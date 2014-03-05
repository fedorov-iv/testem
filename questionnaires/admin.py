# -*- coding: utf-8 -*-
from django.contrib import admin
from questionnaires.models import Questionnaire, Question, AnswerVariant, UserAnswer


class AnswerVariantInLine(admin.StackedInline):
    model = AnswerVariant
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    #набор полей списка
    list_display = ('title',)

    #выводим панель фильтров
    list_filter = ['questionnaire']

    #выводим панель поиска
    search_fields = ['title']

    inlines = [AnswerVariantInLine]


class QuestionnaireAdmin(admin.ModelAdmin):


    #набор полей списка
    list_display = ('title', 'create_date', 'link_to_objects', 'is_active')

    #выводим панель фильтров
    list_filter = ['create_date', 'is_active']

    #выводим панель поиска
    search_fields = ['title', 'description']


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question, QuestionAdmin)
