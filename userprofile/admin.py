from django.contrib import admin
from django.contrib.auth.models import User
from userprofile.models import *
from django.contrib.auth.admin import UserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'
    max_num = 1

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline,]
    

admin.site.unregister(User)
admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
