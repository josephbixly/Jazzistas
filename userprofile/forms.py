from django.forms import ModelForm
from django.db import models
from userprofile import *
from django import forms
#from widgets import *
from django.contrib.auth.models import User
from userprofile import constants

class UserProfile_form(forms.Form):
	username = forms.CharField(max_length="30")
	password = forms.CharField(widget=forms.PasswordInput)
	eadd = forms.CharField(max_length="100")
	complete_name = forms.CharField(max_length="100")
	nickname = forms.CharField(max_length="50")
	gender = forms.CharField(max_length=10, widget=forms.Select(choices=constants.GENDER))
	picture = forms.ImageField()
	signature = forms.CharField(widget=forms.Textarea)

class Login_form(forms.Form):
	username = forms.CharField(max_length="30")
	password = forms.CharField(widget=forms.PasswordInput)
