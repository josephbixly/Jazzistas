from django.shortcuts import render_to_response
from forum.models import *
from userprofile.models import *
from django.template import RequestContext
from django.contrib.auth.models import User
from forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def index(request):
	types = Type.objects.all()
	if request.user.is_authenticated():
		user = request.user
		profile = Profile.objects.get(user=user)
		return render_to_response('forum/forum_main.html', {'profile': profile, 'types': types}, context_instance = RequestContext(request))
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					profile = Profile.objects.get(user=user)
					return render_to_response('forum/forum_main.html', {'profile': profile, 'types': types}, context_instance = RequestContext(request))
				else:
					error = "Account disabled!"
					return render_to_response('forum/forum_main.html', {'error': error, 'types': types}, context_instance = RequestContext(request))
			else:
				error = "Invalid Credentials entered or account doesn't exist!"
				return render_to_response('forum/forum_main.html',{'types': types, 'error': error}, context_instance = RequestContext(request))

def forum_subject(request, forum_slug):
	subject = Subject.objects.get(slug=forum_slug)
	if request.user.is_authenticated():
		user = request.user
		profile = Profile.objects.get(user=user)
		return render_to_response('forum/forum_subject.html',{'subject': subject, 'profile': profile, 'subject_slug': forum_slug}, context_instance = RequestContext(request))
	else:
		return render_to_response('forum/forum_subject.html',{'subject': subject}, context_instance = RequestContext(request))

def forum_topic(request, forum_slug, topic_slug):
	topics = Topic.objects.get(slug=topic_slug, subject__slug=forum_slug)
	posts = ForumPost.objects.filter(topic=topics.id)
	t_user = User.objects.get(username=topics.posted_by)
	t_posted_by = Profile.objects.get(user=t_user.id)
	topics.num_views = topics.num_views + 1
	topics.save()
	if request.user.is_authenticated():
		user = request.user
		profile = Profile.objects.get(user=user)
		return render_to_response('forum/forum_topic.html',{'posts': posts, 't_posted_by': t_posted_by, 'topics': topics, 'subject_slug': forum_slug, 'topic_slug': topic_slug, 'profile': profile}, context_instance = RequestContext(request))
	else:
		return render_to_response('forum/forum_topic.html',{'posts': posts, 't_posted_by': t_posted_by, 'topics': topics, 'subject_slug': forum_slug, 'topic_slug': topic_slug}, context_instance = RequestContext(request))

def post_replies(request, forum_slug, topic_slug):
	topics = Topic.objects.get(slug=topic_slug, subject__slug=forum_slug)
	if request.method == 'POST':
		form = ForumPost_Form(request.POST)
		if form.is_valid():
			post = ForumPost(posted_by=request.user,topic=topics,message=form.cleaned_data['message'])
			post.save()
			
	else:
		form = ForumPost_Form()
	
	return render_to_response('forum/post_forum.html', {'form': form}, context_instance = RequestContext(request))

def newthread(request, forum_slug):
	subject = Subject.objects.get(slug=forum_slug)
	if request.method == 'POST':
		form = TopicPost_Form(request.POST)
		if form.is_valid():
			post = Topic(title=form.cleaned_data['title'],status='open',subject=subject,posted_by=request.user,message=form.cleaned_data['message'])
			post.save()
			
	else:
		form = TopicPost_Form()
		
	return render_to_response('forum/post_topic.html', {'form': form}, context_instance = RequestContext(request))

def logout_account(request):
	types = Type.objects.all()
	logout(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				profile = Profile.objects.get(user=user)
				return render_to_response('forum/forum_main.html', {'profile': profile, 'types': types}, context_instance = RequestContext(request))
			else:
				error = "Account disabled!"
				return render_to_response('forum/forum_main.html', {'error': error, 'types': types}, context_instance = RequestContext(request))
		else:
			error = "Invalid Credentials entered or account doesn't exist!"
			return render_to_response('forum/forum_main.html',{'types': types, 'error': error}, context_instance = RequestContext(request))
	else:	
		return render_to_response('forum/forum_main.html',{'types': types}, context_instance = RequestContext(request))
	
