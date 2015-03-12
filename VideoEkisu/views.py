from VideoEkisu import permissions, utilities
from rest_framework import viewsets

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