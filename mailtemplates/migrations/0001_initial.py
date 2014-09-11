# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MailTemplate'
        db.create_table(u'mailtemplates_mailtemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 11, 0, 0))),
            ('from_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('from_email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('admin_email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('copy_emails', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'mailtemplates', ['MailTemplate'])


    def backwards(self, orm):
        # Deleting model 'MailTemplate'
        db.delete_table(u'mailtemplates_mailtemplate')


    models = {
        u'mailtemplates.mailtemplate': {
            'Meta': {'ordering': "['id']", 'object_name': 'MailTemplate'},
            'admin_email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'body': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'copy_emails': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 11, 0, 0)'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mailtemplates']