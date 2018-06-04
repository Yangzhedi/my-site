#coding=utf-8
import json
import datetime
from django.shortcuts import render
from django.db import models

from django.views.decorators.csrf import csrf_protect
from django.core.handlers.wsgi import WSGIRequest

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



def get_all_blogs(request):
    blog_querySet = BlogsPost.objects.all()

    request_dict = json.loads(request.body.decode())

    blog_list = list(blog_querySet.values())
    print(request_dict["page"])
    print(request_dict["size"])

    result = blog_list2json(blog_list)

    # return HttpResponse("get_all_blogs")
    return HttpResponse(json.dumps(result))


def blog_list2json(blog_list):
    result = []
    for i, value in enumerate(blog_list):
        blog = {
            "id": value["id"],
            "title": value["title"],
            "content": value["content"],
            "create_time": value["create_time"].strftime('%Y-%m-%d'),
            "modify_time": value["modify_time"].strftime('%Y-%m-%d'),
            "views": value["views"],
            "timestamp": value["timestamp"].strftime('%Y-%m-%d'),
            # "tag": value["tag"],
            "classification": value["classification"],
            "description": value["description"],
        }
        result.append(blog)
    return result
