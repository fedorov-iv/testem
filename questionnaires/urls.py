# -*- coding: utf8 -*-
from django.conf.urls import *
from questionnaires import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='account'),
    #url(r'^success/$', views.success, name='registration_success'),
    #url(r'^activate/(?P<username>\w+)/$', views.activate, name='registration_activate'),


)