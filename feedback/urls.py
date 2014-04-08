# -*- coding: utf8 -*-
from django.conf.urls import *
from feedback import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='feedback_index'),
)