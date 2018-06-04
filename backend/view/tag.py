#coding=utf-8
import json
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db import models

from django.shortcuts import render_to_response
from django.template import loader,Context

from backend.models import Tag
#  获取user
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry

# model 2 dict
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.core import serializers


def get_all_tags(request):
    print(request.POST)
    tag_list = Tag.objects.all()
    print(tag_list)
    print(tag_list.values())
    for i in tag_list.values():
        print(i['title'])
    return HttpResponse("get_all_tags")


def create_tag(request):
    print(Tag)
    tag_list = Tag.objects.all()
    # 创建tag
    Tag.objects.create(title='yangmv')

    return HttpResponse("get_all_tags")