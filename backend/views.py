#coding=utf-8
import json
from django.core.paginator import Paginator
from django.shortcuts import render
# from blog.models import BlogsPost
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
import time
import csv
from django.http import StreamingHttpResponse


def hello(request):
    return HttpResponse("Hello world")