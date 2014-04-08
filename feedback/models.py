# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime


class Feedback(models.Model):
    subject = models.CharField(verbose_name=u'Тема', max_length=255)
    author_email = models.EmailField(verbose_name=u'E-mail', blank=True)
    user = models.ForeignKey(User, default=None, blank=True, null=True)
    body = models.TextField(verbose_name=u'Сообщение')
    create_date = models.DateTimeField(verbose_name=u'Дата создания', default=datetime.datetime.now())

    class Meta:
        verbose_name = u'сообщение обратной связи'
        verbose_name_plural = u'сообщения обратной связи'