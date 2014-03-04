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

    class Meta:
        verbose_name = u'тест'
        verbose_name_plural = u'тесты'


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    title = tinymce_models.HTMLField(verbose_name=u'Текст вопроса')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'вопрос теста'
        verbose_name_plural = u'вопросы теста'


class AnswerVariant(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(verbose_name=u'Текст варианта ответа', max_length=1000)
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

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'заполненный тест'
        verbose_name_plural = u'заполненные тесты'


class UserAnswerItem(models.Model):
    question = models.ForeignKey(Question, verbose_name=u'Вопрос теста')
    answer_variant = models.ForeignKey(AnswerVariant, verbose_name=u'Вариант ответа')
    user_answer = models.ForeignKey(UserAnswer, verbose_name=u'Заполненный тест')
    weight = models.IntegerField(verbose_name=u'Вес', default=0)

    def __unicode__(self):
        return u'Ответ пользователя'

    class Meta:
        verbose_name = u'ответ пользователя'
        verbose_name_plural = u'ответ пользователя'