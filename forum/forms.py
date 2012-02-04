from django.forms import ModelForm
from django.db import models
from models import *
from django import forms
from widgets import *
from django.contrib.auth.models import User

class ForumPost_Form(forms.Form):
	message = forms.CharField(widget=AdvancedEditor())
	
class TopicPost_Form(forms.Form):
	title = forms.CharField()
	message = forms.CharField(widget=AdvancedEditor())
	
	
	

