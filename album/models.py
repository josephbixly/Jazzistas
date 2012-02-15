from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from album import constants

class Gallery(models.Model):
    title = models.CharField(max_length = 50)
    desc = models.TextField(null = True, blank = True)
    slug = models.SlugField(null = True, blank = True)
    
    def __unicode__(self):
		return self.title
		
    def save(self):
		self.slug = '%s' % (slugify(self.title))
		super(Gallery, self).save()
    
class Image(models.Model):
    gallery = models.ForeignKey(Gallery)
    img = models.ImageField(upload_to = constants.UPLOAD_TO, blank = True)
    img_name = models.CharField(max_length = 30)
    desc = models.TextField(null = True, blank = True)
    slug = models.SlugField(null = True, blank = True)
    
    def __unicode__(self):
		return self.img_name
    
class Comment(models.Model):
	image = models.ForeignKey(Image)
	comment = models.TextField(null = True, blank = True)
	posted_by = models.ForeignKey(User)
	posted_date = models.DateField(auto_now_add = True)
