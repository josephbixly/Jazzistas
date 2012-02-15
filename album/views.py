from django.shortcuts import render_to_response
from album.models import *
from userprofile.models import *
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.defaultfilters import slugify
from forms import *
from django.contrib.auth.decorators import login_required


"""def index(request):
	user = request.user
	profile = Profile.objects.get(user=user)
	return render_to_response('album/album_main.html',{'profile': profile},context_instance = RequestContext(request))"""

@login_required
		
def view_all(request):
	gallery = Gallery.objects.all()
	user = request.user
	profile = Profile.objects.get(user=user)
	gallery = Gallery.objects.all()
	return render_to_response('album/gallery_main.html',{'profile': profile, 'gallery': gallery},context_instance = RequestContext(request))
		
def view_gallery(request, gallery_slug):
	user = request.user
	profile = Profile.objects.get(user=user)
	gallery = Gallery.objects.get(slug=gallery_slug)
	photos = Image.objects.filter(gallery=gallery.id)
	return render_to_response('album/album.html',{'gallery': gallery, 'photos': photos, 'profile': profile},context_instance = RequestContext(request))
		
def upload_picture(request, gallery_slug):
	gallery = Gallery.objects.get(slug=gallery_slug)
	if request.method == 'POST':
		form = Upload_Form(request.POST, request.FILES)
		if form.is_valid():
			img = form.save(commit = False)
			img.gallery = gallery
			img.save()
	else:
		form = Upload_Form()
	
	return render_to_response('album/upload.html',{'form': form},context_instance = RequestContext(request))
	
	
