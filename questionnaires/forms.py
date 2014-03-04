# -*- coding: utf8 -*-
from questionnaires.models import Questionnaire
from django import forms


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label=u"Название теста")
        self.fields['description'] = forms.CharField(label=u"Описание теста", widget=forms.Textarea, required=False)
