# coding:utf-8
# from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Guest(BaseModel):
    avatar = models.CharField(max_length=256, default='/s/image/avatar.png')
    nick = models.CharField(max_length=128)
    email = models.CharField(max_length=256, null=True, blank=True)
    forbid = models.BooleanField(default=False)
    token = models.CharField(max_length=64, unique=True)
    uid = models.IntegerField(unique=True)

    def __unicode__(self):
        return '{0}-{1}'.format(self.nick, self.email)


class Tag(BaseModel):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class BlogsPost(BaseModel):
    title = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='tag_arts')
    # author = models.CharField(max_length=50, default='Timi')
    timestamp = models.DateTimeField(default=None)
    # blog_id = models.IntegerField(default=0)
    classification = models.CharField(max_length=10, default=u'原创')
    content = models.TextField()


class Comment(BaseModel):
    content = models.TextField()
    author = models.ForeignKey(Guest, related_name='user_comments', null=True, blank=True, on_delete=models.SET_NULL)
    belong = models.ForeignKey(BlogsPost, related_name='art_comments', on_delete=models.DO_NOTHING)
    state = models.CharField(max_length=64, null=True, blank=True)
    review = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0}-{1}'.format(self.author, self.create_time.strftime("%Y-%m-%d %H:%M:%S"))

class BlogPostAdmin(object):
    list_display = ('id', 'title', 'timestamp')


# admin.site.register(BlogPostAdmin)
