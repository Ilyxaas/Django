from django.contrib import admin

# Register your models here

from .models import Post
from .models import Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_create', 'photo', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['time_create', 'title']

    list_filter = ['is_published']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
