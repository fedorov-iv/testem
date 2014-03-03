# -*- coding: utf8 -*-
from django.db import models
import datetime
from tinymce import models as tinymce_models


class MailTemplate(models.Model):
    #список полей модели
    title = models.CharField(u'Название', max_length=255)
    code = models.CharField(u'Символьный код', max_length=255)
    create_date = models.DateTimeField(u'Дата создания', default=datetime.datetime.now())
    from_name = models.CharField(u'От (имя)', max_length=255)
    from_email = models.EmailField(u'От (e-mail)', max_length=255)
    admin_email = models.EmailField(u'Кому (e-mail)', max_length=255)
    copy_emails = models.CharField(u'Копия (e-mail)', max_length=255, help_text=u'Если несколько, разделитель - точка с запятой', blank=True)
    subject = models.CharField(u'Тема письма', max_length=255)
    body = tinymce_models.HTMLField(u'Текст сообщения', blank=True)

    #Задаём название полей и порядок
    class Meta:
        verbose_name = u'почтовый шаблон'
        verbose_name_plural = u'почтовые шаблоны'
        ordering = ['id']

    def __unicode__(self):
        return self.title