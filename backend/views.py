#coding=utf-8
import json
from django.core.paginator import Paginator
from django.shortcuts import render
# from blog.models import BlogsPost
from backend.models import BlogsPost
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from django.core import serializers
import time
import csv
from django.http import StreamingHttpResponse


def hello(request):
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