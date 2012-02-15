from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^main/', include('jazz.urls')),
	url(r'^album/', include('album.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('userprofile.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
