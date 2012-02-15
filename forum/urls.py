from django.conf.urls.defaults import *

urlpatterns = patterns('forum.views',
    url(r'^$', 'index'),
    url(r'^logout/', 'logout_account'),
    url(r'(?P<forum_slug>[\w-]+)/(?P<topic_slug>[\w-]+)/(?P<post_id>\d+)/remove_post$', 'remove_post'),
    url(r'(?P<forum_slug>[\w-]+)/(?P<topic_slug>[\w-]+)/remove$', 'remove_thread'),
	url(r'(?P<forum_slug>[\w-]+)/(?P<topic_slug>[\w-]+)/post$', 'post_replies'),
    url(r'(?P<forum_slug>[\w-]+)/(?P<topic_slug>[\w-]+)/$', 'forum_topic'),
    url(r'(?P<forum_slug>[\w-]+)/newthread$', 'newthread'),
    url(r'(?P<forum_slug>[\w-]+)/$', 'forum_subject'),
)

