from django.db import models
from django.contrib.auth.models import User
from userprofile import constants

class Profile(models.Model):
    user = models.ForeignKey(User)
    complete_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=constants.GENDER)
    type = models.CharField(max_length=50, choices=constants.USER_TYPES)
    picture = models.ImageField(upload_to = "%s/profile_pictures" % (constants.UPLOAD_TO))
    signature = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return self.user.username
