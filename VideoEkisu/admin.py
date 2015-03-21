from django.http import HttpResponse
from django.shortcuts import render
from VideoEkisu import notification

__author__ = 'seung-wongim'

from django.contrib import admin
from .models import Video, Ekisu, Device


def push_admin(request, *args, **kwargs):
    if request.method == 'GET':
        device_list = Device.objects.order_by('id')
        context = {'device_list': device_list}
        return render(request, 'push.html', context)
    else:
        message = request.POST['message']
        notification.send_message(message=message)
        return HttpResponse('complete')
admin.site.register_view('push', 'Push notification', view=push_admin)


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