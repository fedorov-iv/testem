# -*- coding: utf-8 -*-
from django.contrib import admin
from mailtemplates.models import MailTemplate


class MailTemplatesAdmin(admin.ModelAdmin):


    #набор полей списка
    list_display = ('title', 'create_date', 'code')

    #выводим панель фильтров
    list_filter = ['create_date']

    #выводим панель поиска
    search_fields = ['title']


admin.site.register(MailTemplate, MailTemplatesAdmin)
