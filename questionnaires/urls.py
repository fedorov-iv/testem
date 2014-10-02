# -*- coding: utf8 -*-
from django.conf.urls import *
from questionnaires import views

urlpatterns = patterns('',

    #  административные
    url(r'^$', views.index, name='account'),
    url(r'^data/$', views.index_data, name='account_data'),
    url(r'^createtest/$', views.create_test, name='create_test'),
    url(r'^createtest/(?P<questionnaire_id>[1-9]\d*)/$', views.create_test, name='create_test'),
    url(r'^deletetest/$', views.delete_test, name='delete_test'),
    url(r'^deletetest/(?P<questionnaire_id>[1-9]\d*)/$', views.delete_test, name='delete_test'),
    url(r'^createquestions/$', views.create_questions, name='create_questions'),
    url(r'^createquestions/(?P<questionnaire_id>[1-9]\d*)/$', views.create_questions, name='create_questions'),
    url(r'^getquestiondetails/(?P<question_id>[1-9]\d*)/$', views.get_question_details, name='get_question_details'),
    url(r'^deletequestion/$', views.delete_question, name='delete_question'),
    url(r'^deletequestion/(?P<question_id>[1-9]\d*)/$', views.delete_question, name='delete_question'),

)