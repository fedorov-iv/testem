# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Questionnaire'
        db.create_table(u'questionnaires_questionnaire', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('description', self.gf('tinymce.models.HTMLField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 5, 0, 0))),
        ))
        db.send_create_signal(u'questionnaires', ['Questionnaire'])

        # Adding model 'Question'
        db.create_table(u'questionnaires_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaires.Questionnaire'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('description', self.gf('tinymce.models.HTMLField')()),
            ('ord', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'questionnaires', ['Question'])

        # Adding model 'AnswerVariant'
        db.create_table(u'questionnaires_answervariant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaires.Question'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('is_correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'questionnaires', ['AnswerVariant'])

        # Adding model 'UserAnswer'
        db.create_table(u'questionnaires_useranswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 5, 0, 0))),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaires.Questionnaire'])),
            ('test_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('user_srore', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'questionnaires', ['UserAnswer'])


    def backwards(self, orm):
        # Deleting model 'Questionnaire'
        db.delete_table(u'questionnaires_questionnaire')

        # Deleting model 'Question'
        db.delete_table(u'questionnaires_question')

        # Deleting model 'AnswerVariant'
        db.delete_table(u'questionnaires_answervariant')

        # Deleting model 'UserAnswer'
        db.delete_table(u'questionnaires_useranswer')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'questionnaires.answervariant': {
            'Meta': {'object_name': 'AnswerVariant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questionnaires.Question']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'questionnaires.question': {
            'Meta': {'ordering': "['ord']", 'object_name': 'Question'},
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ord': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questionnaires.Questionnaire']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'questionnaires.questionnaire': {
            'Meta': {'object_name': 'Questionnaire'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 5, 0, 0)'}),
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'questionnaires.useranswer': {
            'Meta': {'object_name': 'UserAnswer'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 5, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questionnaires.Questionnaire']"}),
            'test_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'user_srore': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['questionnaires']