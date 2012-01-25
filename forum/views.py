from django.shortcuts import render_to_response
from forum.models import *
from django.template import RequestContext
#from forms import *

def index(request):
	types = Type.objects.all()
	return render_to_response('forum/forum_main.html',{'types': types}, context_instance = RequestContext(request))
	
def forum_topic(request):
	topic = Topic.objects.all()
	return render_to_response('forum/forum_topic.html',{'forum': forum}, context_instance = RequestContext(request))

