from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^zoom/', include('zoom.urls', namespace='zoom')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
    url('', include('home.urls', namespace='home')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)