from VideoEkisu import permissions, notification
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
    permission_classes = (permissions.IsAdminOrWriteOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        device = request.data
        # register device token and get arn from Amazon SNS.
        arn = notification.get_arn(device_token=device['token'], device_type=device['type'])
        # replace arn data to new arn.
        serializer.validated_data['arn'] = arn
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)