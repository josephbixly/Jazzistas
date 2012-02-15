from django.conf.urls.defaults import *

urlpatterns = patterns('userprofile.views',
    url(r'login/$', 'login'),
    url(r'logout/$', 'logout'),
    url(r'register/$', 'register'),
)

