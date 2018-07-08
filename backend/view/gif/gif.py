#coding=utf-8

# model 2 dict
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.core import serializers


# from gif.pngaddtext import main
from . import pngaddtext


def create_gif(request):
    # print(request.POST)
    # words_dict = model_to_dict(request.POST.dict())
    value = list(request.POST.dict().values())
    print(value)
    # print(model_to_dict(request.POST))
    pngaddtext.main(value)
    return HttpResponse("create_gif")

