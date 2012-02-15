from django.contrib import admin
from album.models import *


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    inlines = [ImageInline,]

    
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image)
