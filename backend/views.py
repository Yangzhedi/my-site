#coding=utf-8
import json
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db import models

from django.shortcuts import render_to_response
from django.template import loader,Context

from backend.models import BlogsPost
#  获取user
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry

# model 2 dict
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.core import serializers

# 检查密码
from django.contrib.auth.hashers import make_password, check_password
import time
import csv
from django.http import StreamingHttpResponse


def hello(request):
    print(User)
    user_list = User.objects.all()
    print(user_list)
    print(user_list.values())

    yzd = User.objects.get(username='yzd')
    yzd_dict = model_to_dict(yzd)
    print(yzd_dict['password'])
    ps = "yzd1611163"
    dj_ps = make_password(ps, None, 'pbkdf2_sha256')
    ps_bool = check_password(ps, yzd_dict['password'])
    print(dj_ps)
    print(ps_bool)
    if ps_bool:
        print(HttpResponse(yzd_dict))
        return HttpResponse(yzd_dict)
    else:
        return HttpResponse("Hello world")


def test(request):
    # .values 获取值
    user_list = LogEntry.objects.values()
    print(user_list)
    for i in user_list:
        print(i['object_repr'])
    return HttpResponse("Hello world")

def blog1(request):
    blog_list = BlogsPost.objects.all()
    post = blog_list2json(blog_list)
    print(post)
    postData = {
        'status': 200,
        'result': post
    }
    response = HttpResponse(json.dumps(postData))
    ajax_testvalue = serializers.serialize("json",blog_list[0])
    return HttpResponse(response)


def ajax_time(request):
    blog_list = BlogsPost.objects.all()
    time_list = []
    for i in blog_list:
        time_list.append(i.timestamp.strftime("%Y%m%d%H%M%S"))
        print(i)
    return HttpResponse(json.dumps({"time":time_list}))


def blog_list2json(blog_list):
    result = []
    for i, value in enumerate(blog_list):
        blog = {
            # "id": value.id,
            "title": value.title,
            "content": value.content,
            # "author": value.author,
            "timestamp": value.timestamp.strftime('%Y-%m-%d'),
            # "tags": value.tags,
            "classification": value.classification
        }
        result.append(blog)
    return result