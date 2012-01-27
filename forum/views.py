from django.shortcuts import render_to_response
from forum.models import *
from django.template import RequestContext
#from forms import *

def index(request):
	types = Type.objects.all()
	return render_to_response('forum/forum_main.html',{'types': types}, context_instance = RequestContext(request))
	
def forum_subject(request, forum_slug):
	subject = Subject.objects.get(slug=forum_slug)
	topic = Topic.objects.get(subject=subject.id)
	tid = topic.id
	views = Topic.objects.get(id=tid).num_views
	return render_to_response('forum/forum_subject.html',{'subject': subject, 'views': views}, context_instance = RequestContext(request))

def forum_topic(request, subject_slug, topic_slug):
	subject = Subject.objects.get(slug=subject_slug)
	topic = Topic.objects.get(slug=topic_slug)
	return render_to_response('forum/forum_topic.html',{'topic': topic}, context_instance = RequestContext(request))
