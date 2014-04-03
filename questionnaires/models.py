# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
import datetime


class Questionnaire(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(verbose_name=u'Название', max_length=1000)
    description = tinymce_models.HTMLField(verbose_name=u'Описание')
    is_active = models.BooleanField(verbose_name=u'Активно')
    create_date = models.DateTimeField(verbose_name=u'Дата создания', default=datetime.datetime.now())

    def __unicode__(self):
        return self.title

    def link_to_objects(self):
        return '<a href="/admin/questionnaires/question/?questionnaire={0}">{1} => </a>'.format(self.pk, self.objects_count())
    link_to_objects.short_description = u'Вопросы теста'
    link_to_objects.allow_tags = True

    def objects_count(self):
        return Question.objects.filter(questionnaire=self.pk).count()

    class Meta:
        verbose_name = u'тест'
        verbose_name_plural = u'тесты'


class Question(models.Model):
    author = models.ForeignKey(User)
    questionnaire = models.ForeignKey(Questionnaire)
    title = models.CharField(verbose_name=u'Краткое название', max_length=1000)
    description = tinymce_models.HTMLField(verbose_name=u'Текст вопроса')
    ord = models.IntegerField(verbose_name=u'Порядок сортировки', default=0)

    def __unicode__(self):
        return self.title

    def objects_count(self):
        return AnswerVariant.objects.filter(question=self.pk).count()

    class Meta:
        verbose_name = u'вопрос теста'
        verbose_name_plural = u'вопросы теста'
        ordering = ['ord']


class AnswerVariant(models.Model):
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    title = models.CharField(verbose_name=u'Текст варианта ответа', max_length=1000, )
    is_correct = models.BooleanField(verbose_name=u'Верный ответ', default=False)
    weight = models.IntegerField(verbose_name=u'Вес ответа', default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'вариант ответа'
        verbose_name_plural = u'вариант ответа'


class UserAnswer(models.Model):
    author = models.ForeignKey(User, verbose_name=u'Пользователь')
    title = models.CharField(verbose_name=u'Название теста', max_length=1000)
    create_date = models.DateTimeField(verbose_name=u'Дата прохождения', default=datetime.datetime.now())
    questionnaire = models.ForeignKey(Questionnaire, verbose_name=u'Тест')
    #  максимально возможное количество баллов в тесте
    test_score = models.IntegerField(verbose_name=u'Максимальный балл теста', default=0)
    #  количество баллов, набранное пользователем в тесте
    user_score = models.IntegerField(verbose_name=u'Набранные баллы', default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'заполненный тест'
        verbose_name_plural = u'заполненные тесты'
