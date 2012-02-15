from django.forms import ModelForm
from django.db import models
from models import *
from django import forms
from django.contrib.auth.models import User

class Upload_Form(forms.ModelForm):
	class Meta:
		model = Image
		exclude = ('gallery','slug')
