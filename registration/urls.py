# -*- coding: utf8 -*-
from django.conf.urls import *
from registration import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='registration_index'),
    url(r'^success/$', views.success, name='registration_success'),
    url(r'^activate/(?P<username>\w+)/$', views.activate, name='registration_activate'),


)