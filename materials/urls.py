# -*- coding: utf8 -*-
from django.conf.urls import *
from materials import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='mymaterials'),


)