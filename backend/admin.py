from django.contrib import admin
from backend.models import *
import xadmin

admin.site.register(BlogsPost, BlogPostAdmin)
admin.site.register(Tag)