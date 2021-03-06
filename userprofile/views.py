from django.shortcuts import render_to_response
from django.http import HttpResponse
from userprofile.models import *
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.defaultfilters import slugify
from forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_account(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				profile = Profile.objects.get(user=user)
				return render_to_response('jazz/index.html',{'profile': profile}, context_instance = RequestContext(request))
		else:
			error = "Invalid Credentials entered or account doesn't exist!"
			return render_to_response('userprofile/login.html',{'error': error}, context_instance = RequestContext(request))
	else:
		return render_to_response('userprofile/login.html', context_instance = RequestContext(request))
		
def logout_account(request):
	logout(request)
	return render_to_response('jazz/index.html', context_instance = RequestContext(request))
	

def register(request):
	if request.method == "POST":
		form = UserProfile_form(request.POST, request.FILES)
		if form.is_valid():
			user = User(username=form.cleaned_data["username"], password=form.cleaned_data["password"], email=form.cleaned_data["eadd"])
			user.save()
			profile = Profile(user=user, complete_name=form.cleaned_data["complete_name"], nickname=form.cleaned_data["nickname"], gender=form.cleaned_data["gender"], type='Member', picture=form.cleaned_data["picture"], signature=form.cleaned_data["signature"])
			profile.save()
	else:
		form = UserProfile_form()
	
	return render_to_response('userprofile/register.html',{'form':form},context_instance = RequestContext(request))
