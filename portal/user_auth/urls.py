from django.conf.urls import url, patterns

from . import views 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/', views.user_create, name='add_user'),
    url(r'^login/', views.login_page, name='login_page'),
    url(r'^auth/', views.user_auth, name='user_auth'),
)