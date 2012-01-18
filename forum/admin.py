from django.contrib import admin
from forum.models import *

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(ForumPost)
admin.site.register(Type)
