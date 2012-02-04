from django.contrib import admin
from forum.models import *

class SubjectClass(admin.ModelAdmin):
	fields = ['title', 'status', 'type', 'posted_by']
	
class TopicClass(admin.ModelAdmin):
	fields = ['title', 'status', 'subject', 'posted_by', 'message']

admin.site.register(Subject, SubjectClass)
admin.site.register(Topic, TopicClass)
admin.site.register(ForumPost)
admin.site.register(Type)
