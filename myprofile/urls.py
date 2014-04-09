# -*- coding: utf8 -*-
from django.conf.urls import *
from myprofile import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='user_profile'),

)