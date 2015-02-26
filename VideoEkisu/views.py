from VideoEkisu import permissions
from rest_framework import viewsets

__author__ = 'seung-wongim'

from VideoEkisu.models import Video, Ekisu, EkisuSerializer, VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)


class EkisuViewSet(viewsets.ModelViewSet):
    queryset = Ekisu.objects.all()
    serializer_class = EkisuSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)
