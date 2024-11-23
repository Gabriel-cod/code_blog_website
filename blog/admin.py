from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Post


class PostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'data_creation')
    search_fields = ('title', 'author', 'data_creation') 
    
admin.site.register(Post, PostAdmin)
