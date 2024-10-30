from django.contrib import admin
from .models import Image, Notes
from django.contrib.admin import ModelAdmin

class NotesAdmin(admin.ModelAdmin):
    list_display=['plantname', 'description', 'image']

admin.site.register(Notes, NotesAdmin)
admin.site.register(Image)