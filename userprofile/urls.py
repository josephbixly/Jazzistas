from django.conf.urls.defaults import *

urlpatterns = patterns('userprofile.views',
    url(r'login/$', 'login_account'),
    url(r'logout/$', 'logout_account'),
    url(r'register/$', 'register'),
)

