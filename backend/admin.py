from django.contrib import admin
from backend.models import *
import xadmin

xadmin.site.register(BlogsPost, BlogPostAdmin)
xadmin.site.register(Tag)