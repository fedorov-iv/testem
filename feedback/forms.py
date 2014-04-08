# -*- coding: utf8 -*-
from feedback.models import Feedback
from django import forms
from captcha.fields import CaptchaField


class FeedbackForm(forms.ModelForm):

        captcha = CaptchaField()

        class Meta:
            model = Feedback
            fields = ['subject', 'body', 'author_email']

        def __init__(self, user=None, *args, **kwargs):
            super(FeedbackForm, self).__init__(*args, **kwargs)
            self._user = user

        def clean_author_email(self):
            if self._user.is_authenticated():
                return self._user.email
            elif self.cleaned_data.get('author_email'):
                return self.cleaned_data.get('author_email')
            else:
                raise forms.ValidationError("Обязательное поле.")
