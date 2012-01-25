from django.db import models
from django.contrib.auth.models import User

class Blogpost(models.Model):
	title = models.CharField(max_length = 50),
	posted_by = models.ForeignKey(User),
	posted_date = models.DateField(auto_now_add = True),
	message = models.CharField(max_length = 1000)
	 
	def __unicode__(self):
		return '%s %s %s %s' % (self.title, self.posted_by, self.posted_date, self.message)
	 

class Comments(models.Model):
	comment = models.CharField(max_length = 300),
	posted_by = models.ForeignKey(User),
	posted_date = models.DateField(auto_now_add = True)
	 
	def __unicode__(self):
		return '%s %s %s' % (self.comment, self.posted_by, self.posted_date)
