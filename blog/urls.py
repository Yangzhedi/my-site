"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from backend.feeds import BlogRssFeed
from backend.views import hello, blog1, ajax_time

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^$', TemplateView.as_view(template_name="index.html"))
# ]

# -*- coding: utf-8 -*-
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    # url('admin/', admin.site.urls),
    url(r'xadmin/', xadmin.site.urls),
    url(r'^rss/$', BlogRssFeed(), name='rss'),


    url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^login$',TemplateView.as_view()),

    url(r'^hello/$', hello),
    url(r'^blog1/$', blog1),
    url(r'^blog2/$', ajax_time),

    # url(r'^api/', include('backend.urls', namespace='api'))
]