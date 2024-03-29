import os
import requests
from django.http import HttpResponse
from django.shortcuts import render

__author__ = 'seung-wongim'

from django.contrib import admin
from .models import Video, Ekisu, Device


def push_admin(request, *args, **kwargs):
    device_list = Device.objects.order_by('id')
    if request.method == 'GET':
        context = {'device_list': device_list}
        return render(request, 'push.html', context)
    else:
        message = request.POST['message']
        for device in device_list:
            send_push(device=device.token, message=message)
        return HttpResponse('complete')
admin.site.register_view('push', 'Push notification', view=push_admin)


def send_push(device, message):
    post_data = {'token': os.environ.get('APNS_PROD_TOKEN'),
                 'message': message,
                 'badge': 1,
                 'device': device}
    response = requests.post('http://push.anbado.com/push/to-single-device', data=post_data)
    content = response.content
    return HttpResponse(content)


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'duration', ]
    list_editable = ['title']
    search_fields = ['title']
    ordering = ['title']


class EkisuAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']
    list_filter = ['video']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    ordering = ['-created']


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'token']
    list_filter = ['type']
    list_display_links = ['token']
    search_fields = ['id', 'token']
    ordering = ['id']


admin.site.register(Video, VideoAdmin)
admin.site.register(Ekisu, EkisuAdmin)
admin.site.register(Device, DeviceAdmin)