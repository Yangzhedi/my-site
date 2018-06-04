#coding=utf-8
import json
import datetime
from django.shortcuts import render
from django.db import models

from django.views.decorators.csrf import csrf_protect


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


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

# @csrf_protect
def login(request):
    print(request.POST)
    print(type(request.POST.get('user')))
    print(request.content_type)
    # print(User)  == 'application/x-www-form-urlencoded'
    user_list = User.objects.all()
    # print(user_list)
    # print(user_list.values())

    username = request.POST.get('user')
    user_model = User.objects.get(username=username)
    # if user_model:

    user_dict = model_to_dict(user_model)

    print(user_dict['password'])
    ps = request.POST.get('password')
    print(ps)
    dj_ps = make_password(ps, None, 'pbkdf2_sha256')
    ps_bool = check_password(ps, user_dict['password'])
    print(dj_ps)
    print(ps_bool)
    if ps_bool:
        return HttpResponse(json.dumps(user_dict, default=datetime_handler))
    else:
        return HttpResponse("密码错误")