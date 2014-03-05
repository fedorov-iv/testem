# -*- coding: utf8 -*-
from django.conf.urls import *
from questionnaires import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='account'),
    url(r'^createtest/$', views.create_test, name='create_test'),
    url(r'^createquestions/$', views.create_questions, name='create_questions'),

)