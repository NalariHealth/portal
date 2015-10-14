from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'new/', views.new, name='new'),
    url(r'new_feed/', views.new_feed, name='new_feed'),
    url(r'new_practice/', views.new_practice, name='new_practice'),
    url(r'new_provider/', views.new_provider, name='new_provider'),
    url(r'new_member/', views.new_member, name='new_member'),
    url(r'new_rel/', views.new_pprel, name='new_rel'),
    url(r'select_feed/', views.select_feed, name='select_feed'),
    url(r'edit_feed/', views.edit_feed, name='edit_feed'),
    url(r'select_practice/', views.select_practice, name='select_practice'),
    url(r'edit_practice/', views.edit_practice, name='edit_practice'),
    url(r'select_provider/', views.select_provider, name='select_provider'),
    url(r'edit_provider/', views.edit_provider, name='edit_provider'),
    url(r'select_member/', views.select_member, name='select_member'),
    url(r'edit_member/', views.edit_member, name='edit_member'),
    url(r'select_practice_for_rel/', views.select_practice_for_rel, name='select_practice_for_rel'),
    url(r'delete_rel/', views.delete_rel, name='delete_rel'),
    url(r'select_rel', views.select_rel, name='select_rel'),
    url(r'edit_rel', views.edit_rel, name='edit_rel'),
    url(r'view_feed', views.view_feed, name='view_feed'),
    url(r'delete_feed', views.delete_feed, name='delete_feed'),
    url(r'delete_member', views.delete_member, name='delete_member'),
    url(r'delete_practice', views.delete_practice, name='delete_practice'),
    url(r'delete_provider', views.delete_provider, name='delete_provider'),
    url(r'', views.new, name='new'),
)