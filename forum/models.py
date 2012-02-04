from django.db import models
from django.contrib.auth.models import User
from forum import constants
from django.template.defaultfilters import slugify

class Subject(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=constants.STATUS)
    type = models.ForeignKey('Type')
    posted_by = models.ForeignKey(User)
    posted_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self):
        self.slug = '%s' % (slugify(self.title))
        super(Subject, self).save()

    def __unicode__(self):
        return self.title
    
    def postcount(self):
        count = ForumPost.objects.filter(topic__subject=self).count()
        return count
    
    def lastpostdate(self):
		try:
			lastpost = Topic.objects.filter(topic__subject=self).order_by("posted_date")[0]
			return lastpost
		except:
			return None

class Type(models.Model):
    name = models.CharField(max_length=50)
    access_level = models.CharField(max_length=50, choices=constants.ACCESS_LEVEL)
    
    def __unicode__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=constants.STATUS)
    subject = models.ForeignKey(Subject)
    posted_by = models.ForeignKey(User)
    slug = models.SlugField(blank=True, null=True)
    posted_date = models.DateField(auto_now_add=True)
    num_views = models.IntegerField(default=0)
    message = models.TextField()
    
    def lastpostdate(self):
		try:
			lastpost = ForumPost.objects.filter(forum__topic=self).order_by("posted_date")[0]
			return lastpost
		except:
			return None
    
    def save(self):
        self.slug = '%s' % (slugify(self.title))
        super(Topic, self).save()
        self.slug = '%s-%s' % (self.id, slugify(self.title))
        super(Topic, self).save()
    
    def __unicode__(self):
        return self.title

class ForumPost(models.Model):
    message = models.TextField()
    topic = models.ForeignKey(Topic)
    posted_by = models.ForeignKey(User)
    posted_date = models.DateField(auto_now_add=True)
		
    def __unicode__(self):
        return "%s %s %s" % (self.topic.title, self.posted_by, self.posted_date)
        
