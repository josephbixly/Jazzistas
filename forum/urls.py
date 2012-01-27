from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'forum.views.index'),
    url(r'(?P<forum_slug>[\w-]+)', 'forum.views.forum_subject'),
    url(r'(?P<forum_slug>[\w-]+)/(?P<topic_slug>[\w-]+)', 'forum.views.forum_topic'),
)

