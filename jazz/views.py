from django.shortcuts import render_to_response
from django.http import HttpResponse
#from jazz.models import *
from userprofile.models import *
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.defaultfilters import slugify
#from forms import *

def index(request):
	if not request.user.is_authenticated():
		return render_to_response('jazz/index.html')
	else:
		user = request.user
		profile = Profile.objects.get(user=user)
		return render_to_response('jazz/index.html',{'profile': profile},context_instance = RequestContext(request))
	
def history(request):
	if not request.user.is_authenticated():
		return render_to_response('jazz/history.html')
	else:
		user = request.user
		profile = Profile.objects.get(user=user)
		return render_to_response('jazz/history.html',{'profile': profile},context_instance = RequestContext(request))

def about(request):
	if not request.user.is_authenticated():
		return render_to_response('jazz/about.html')
	else:
		user = request.user
		profile = Profile.objects.get(user=user)
		return render_to_response('jazz/about.html',{'profile': profile},context_instance = RequestContext(request))
	
#def contacts(request):
#	return render_to_response('jazz/contact.html')
