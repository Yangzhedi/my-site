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
from backend.views import hello, blog1, ajax_time, test
from backend.view.tag import get_all_tags, create_tag
from backend.view.blog import get_all_blogs, get_blog_by_id
from backend.view.gif.gif import create_gif
from backend.view.auth import login


# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
#
# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


# -*- coding: utf-8 -*-
# import xadmin
# xadmin.autodiscover()
# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = [
    # url('admin/', admin.site.urls),
    url(r'admin/', admin.site.urls),
    url(r'^rss/$', BlogRssFeed(), name='rss'),


    # url(r'^login$',TemplateView.as_view()),

    url(r'^hello/$', hello),
    url(r'^test/$', test),
    url(r'^blog1/$', blog1),
    url(r'^blog2/$', ajax_time),
    url(r'^api/v1/login$', login),
    url(r'^api/v1/get-all-tags$', get_all_tags),
    url(r'^api/v1/create-tag$', create_tag),
    url(r'^api/v1/get-all-blogs$', get_all_blogs),
    url(r'^api/v1/get-blog$', get_blog_by_id),
    url(r'^api/v1/create-gif$', create_gif),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^(?:.*|!admin/)/?$', TemplateView.as_view(template_name="index.html")),

    # url(r'^api/', include('backend.urls', namespace='api'))
]