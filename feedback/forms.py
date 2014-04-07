# -*- coding: utf8 -*-
from feedback.models import Feedback
from django import forms
from django.contrib.auth. models import User


class FeedbackForm(forms.ModelForm):
        class Meta:
            model = Feedback
            fields = ['subject', 'body', 'author_email']

        def __init__(self, user=None, *args, **kwargs):
            super(FeedbackForm, self).__init__(*args, **kwargs)
            self._user = user

        def clean_author_email(self):
            if self._user.email:
                #user = User.objects.get(username=self._user)
                return self._user.email
            elif self.cleaned_data.get('author_email'):
                return self.cleaned_data.get('author_email')
            else:
                raise forms.ValidationError("Обязательное поле")
