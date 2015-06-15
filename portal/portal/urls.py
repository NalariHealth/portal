from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^zoom/', include('zoom.urls', namespace='zoom')),
    url(r'^home/', include('home.urls', namespace='home')),
    url('', include('home.urls', namespace='home')),
)