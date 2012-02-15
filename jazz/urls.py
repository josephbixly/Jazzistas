from django.conf.urls.defaults import *

urlpatterns = patterns('jazz.views',
    url(r'^$', 'index'),
    url(r'history/$', 'history'),
    url(r'about/$', 'about'),
    url(r'contacts/$', 'contacts'),
)

