from django.shortcuts import render_to_response
from forum.models import *
from django.template import RequestContext
#from forms import *

def index(request):
	types = Type.objects.all()
	return render_to_response('forum/forum_main.html',{'types': types}, context_instance = RequestContext(request))
	
def forum_subject(request, forum_slug):
	print "asfasfas"
	subject = Subject.objects.get(slug=forum_slug)
	topic = Topic.objects.get(subject=subject.id)
	tid = topic.id
	views = Topic.objects.get(id=tid).num_views
	return render_to_response('forum/forum_subject.html',{'subject': subject, 'views': views}, context_instance = RequestContext(request))

def forum_topic(request, forum_slug, topic_slug):
	#posts = ForumPost.objects.filter(topic__subject__slug=subject_slug,topic__slug=topic_slug)
	posts = []
	return render_to_response('forum/forum_topic.html',{'posts': posts}, context_instance = RequestContext(request))
