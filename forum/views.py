from django.shortcuts import render_to_response
from forum.models import *
from userprofile.models import *
from django.template import RequestContext
from django.contrib.auth.models import User
from forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	types = Type.objects.all()
	user = request.user
	profile = Profile.objects.get(user=user)
	return render_to_response('forum/forum_main.html', {'profile': profile, 'types': types}, context_instance = RequestContext(request))
		
def forum_subject(request, forum_slug):
	subject = Subject.objects.get(slug=forum_slug)
	user = request.user
	profile = Profile.objects.get(user=user)
	return render_to_response('forum/forum_subject.html',{'subject': subject, 'profile': profile, 'subject_slug': forum_slug}, context_instance = RequestContext(request))
	
def forum_topic(request, forum_slug, topic_slug):
	topics = Topic.objects.get(slug=topic_slug, subject__slug=forum_slug)
	posts = ForumPost.objects.filter(topic=topics.id)
	t_user = User.objects.get(username=topics.posted_by)
	t_posted_by = Profile.objects.get(user=t_user.id)
	topics.num_views = topics.num_views + 1
	topics.save()
	user = request.user
	profile = Profile.objects.get(user=user)
	return render_to_response('forum/forum_topic.html',{'posts': posts, 't_posted_by': t_posted_by, 'topics': topics, 'subject_slug': forum_slug, 'topic_slug': topic_slug, 'profile': profile}, context_instance = RequestContext(request))

def post_replies(request, forum_slug, topic_slug):
	topics = Topic.objects.get(slug=topic_slug, subject__slug=forum_slug)
	if request.method == 'POST':
		form = ForumPost_Form(request.POST)
		if form.is_valid():
			post = ForumPost(posted_by=request.user,topic=topics,message=form.cleaned_data['message'])
			post.save()
			
	else:
		form = ForumPost_Form()
	
	return render_to_response('forum/post_reply.html', {'form': form, 'topics': topics}, context_instance = RequestContext(request))
	
def remove_post(request, forum_slug, topic_slug, post_id):
	post = ForumPost.objects.get(pk=post_id)
	post.delete()
	topics = Topic.objects.get(slug=topic_slug, subject__slug=forum_slug)
	posts = ForumPost.objects.filter(topic=topics.id)
	t_user = User.objects.get(username=topics.posted_by)
	t_posted_by = Profile.objects.get(user=t_user.id)
	user = request.user
	profile = Profile.objects.get(user=user)
	return render_to_response('forum/forum_topic.html',{'posts': posts, 't_posted_by': t_posted_by, 'topics': topics, 'subject_slug': forum_slug, 'topic_slug': topic_slug, 'profile': profile}, context_instance = RequestContext(request))

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
	
def remove_thread(request, forum_slug, topic_slug):
	topics = Topic.objects.get(slug=topic_slug, subject__slug=forum_slug)
	topics.delete()
	subject = Subject.objects.get(slug=forum_slug)
	user = request.user
	profile = Profile.objects.get(user=user)
	return render_to_response('forum/forum_subject.html',{'subject': subject, 'profile': profile, 'subject_slug': forum_slug, 'user': user}, context_instance = RequestContext(request))
