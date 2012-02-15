from django.conf.urls.defaults import *

urlpatterns = patterns('album.views',
    url(r'^$', 'view_all'),
    #url(r'view/$', 'view_all'),
    #url(r'add/', 'add_new'),
    url(r'view/(?P<gallery_slug>[\w-]+)/$', 'view_gallery'),
    url(r'view/(?P<gallery_slug>[\w-]+)/upload$', 'upload_picture')
)

