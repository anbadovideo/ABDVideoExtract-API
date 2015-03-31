__author__ = 'seung-wongim'

from django.db import models
from rest_framework import serializers
from VideoEkisu import utilities


class Device(models.Model):
    class Meta:
        verbose_name = '디바이스'
        ordering = ['token']
        unique_together = ['token', 'type']

    token = models.CharField(verbose_name='token', max_length=2048, null=False, blank=False, default='')
    type = models.CharField(verbose_name='type', max_length=256, null=False, blank=False, default='')

    def __str__(self):
        return self.token


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        field = ('id', 'token', 'type')


class Video(models.Model):
    class Meta:
        verbose_name = '동영상'
        ordering = ['title']

    identifier = models.CharField(verbose_name='identifier', max_length=256, null=False, blank=False, default='')
    provider = models.CharField(verbose_name='제공자', max_length=512, default='')
    title = models.CharField(verbose_name='제목', max_length=512)
    thumbnail = models.CharField(verbose_name='썸네일', max_length=1024, default='')
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    duration = models.IntegerField(verbose_name='재생시간')

    def __str__(self):
        return self.title


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'identifier', 'provider', 'title', 'thumbnail', 'view_count', 'duration')


class Ekisu(models.Model):
    class Meta:
        verbose_name = '엑기스'
        ordering = ['-created']

    video = models.ForeignKey(Video, verbose_name='엑기스', null=False, blank=False)
    title = models.CharField(verbose_name='제목', max_length=256)
    thumbnail = models.CharField(verbose_name='썸네일', max_length=1024, default='')
    section = models.TextField(verbose_name='구간', max_length=2048, blank=False)
    duration = models.IntegerField(verbose_name='엑기스시간', default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    def __str__(self):
        return self.title


class EkisuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ekisu
        fields = ('id', 'video', 'title', 'thumbnail', 'section', 'duration', 'created')

    video = VideoSerializer(read_only=True)
    duration = serializers.SerializerMethodField()

    def get_duration(self, obj):
        return utilities.ekisu_duration(obj.section)