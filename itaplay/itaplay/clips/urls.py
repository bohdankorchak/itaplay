# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'clips/$', views.list, name='clips'),
    url(r'clips/(?P<pk>\d+)$', views.get_clip, name='get_clip'),
    url(r'delete/(?P<pk>\d+)$', views.clip_delete, name='clip_delete'),
  
)


