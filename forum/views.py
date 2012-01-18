from django.shortcuts import render_to_response
from models import *
from django.template import RequestContext
from forms import *


def index(request):
	return HttpResponse('forum_main.html',context_instance = RequestContext(request))
