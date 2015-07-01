from django.conf.urls import patterns, include, url
import django.contrib.auth.views

from . import views 
from home import views as homeviews

urlpatterns = patterns('',
    # url(r'^login/$', 'django.contrib.auth.views.login', kwargs={'template_name' : 'accounts/login.html'}, name='login'),
    url(r'^login/$', views.my_auth, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page' : '/login/'}),
    url(r'^config/$', views.config, name='config'),
    url(r'', homeviews.home, name='home'),
)