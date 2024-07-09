from django.contrib import admin
from app.models import *

class BlogAdmin(admin.ModelAdmin):
    list_display=('author', 'title', 'text', 'created_at', 'published_at')

admin.site.register(Blog, BlogAdmin)    
