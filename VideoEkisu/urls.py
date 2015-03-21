from VideoEkisu import views
from adminplus.sites import AdminSitePlus
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()
router.register('videos', views.VideoViewSet)
router.register('ekisus', views.EkisuViewSet)
router.register('devices', views.DeviceViewSet)

admin.site = AdminSitePlus()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VideoEkisu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
