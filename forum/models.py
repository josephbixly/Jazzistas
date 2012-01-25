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
    
    def save(self):
        self.slug = '%s' % (slugify(self.name))
        super(Subject, self).save()

    def __unicode__(self):
        return self.title
    
    def postcount(self):
        count = 0
        for topic in self.topic_set.all():
            count += topic.ForumPost_set.count
        return count

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
    slug = models.SlugField(editable=False)
    posted_date = models.DateField(auto_now_add=True)
    
    def save(self):
        self.slug = '%i-%s' % (self.id, slugify(self.title))
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
        
