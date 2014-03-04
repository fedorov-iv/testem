# -*- coding: utf-8 -*-
from django.contrib import admin
from questionnaires.models import Questionnaire, Question, AnswerVariant, UserAnswer, UserAnswerItem


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0


class QuestionnaireAdmin(admin.ModelAdmin):


    #набор полей списка
    list_display = ('title', 'create_date', 'is_active')

    #выводим панель фильтров
    list_filter = ['create_date', 'is_active']

    #выводим панель поиска
    search_fields = ['title', 'description']
    inlines = [QuestionInline]

admin.site.register(Questionnaire, QuestionnaireAdmin)
