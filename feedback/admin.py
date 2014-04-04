# -*- coding: utf-8 -*-
from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):


    #набор полей списка
    list_display = ('subject', 'create_date')

    #выводим панель фильтров
    list_filter = ['create_date']

    #выводим панель поиска
    search_fields = ['subject', 'body']


admin.site.register(Feedback, FeedbackAdmin)
