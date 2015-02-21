__author__ = 'seung-wongim'

from django.contrib import admin
from .models import Video, Ekisu

class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_editable = ['title']
    search_fields = ['title']
    ordering = ['title']


class EkisuAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']
    list_filter = ['video_id']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    ordering = ['-created']


admin.site.register(Video, VideoAdmin)
admin.site.register(Ekisu, EkisuAdmin)