from VideoEkisu import permissions, utilities
from rest_framework import viewsets, status
from rest_framework.response import Response

__author__ = 'seung-wongim'

from VideoEkisu.models import Video, Ekisu, Device, EkisuSerializer, VideoSerializer, DeviceSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)


class EkisuViewSet(viewsets.ModelViewSet):
    queryset = Ekisu.objects.all()
    serializer_class = EkisuSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.WriteOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['arn'] = self.get_arn(request)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_arn(self, request):
        from scarface.models import SNSDevice, APNApplication, GCMApplication

        """
        registers the device to sns
        :param your_device_instance: the device
        :param token: the push token or the registration id
        """
        device = request.data

        # get the correct notification platform
        if device['type'] == 'ios':
            application_platform = APNApplication()
        else:
            application_platform = GCMApplication()

        # register the application
        application_platform.register()

        # create the device resource with the token (may be the push token or the registration id)
        sns_device = SNSDevice(application_platform, device['token'])

        # register the device with sns or update the token/the attributes
        sns_device.register_or_update(new_token=device['token'], custom_user_data="device_id={0}".format('1'))

        # this is important: after updating or registration,
        # your sns resource should have a arn. save this to your database.
        if sns_device.arn:
            return sns_device.arn
        else:
            return 'invalid_arn'