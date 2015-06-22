from django.conf.urls import patterns, include, url
from . import views 

urlpatterns = patterns('',
    url(r'^create/', views.zoom, name='zoom'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^scheduled/', views.scheduled, name='scheduled'),
)