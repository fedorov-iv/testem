# -*- coding: utf8 -*-
from django.conf.urls import *
from questionnaires import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='account'),
    url(r'^page/(?P<page>[1-9]\d*)/$', views.index),
    url(r'^createtest/$', views.create_test, name='create_test'),
    url(r'^createtest/(?P<questionnaire_id>[1-9]\d*)/$', views.create_test, name='create_test'),
    url(r'^deletetest/$', views.delete_test, name='delete_test'),
    url(r'^deletetest/(?P<questionnaire_id>[1-9]\d*)/$', views.delete_test),
    url(r'^createquestions/$', views.create_questions, name='create_questions'),

)