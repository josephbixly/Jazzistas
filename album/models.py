from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length = 50)
    
class Image(models.Model):
    gallery = models.ForeignKey(Gallery)
    comment = models.TextField(null = True, blank = True)
    
