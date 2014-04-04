# -*- coding: utf8 -*-
from feedback.models import Feedback
from django import forms


class FeedbackForm(forms.ModelForm):
        class Meta:
            model = Feedback
            fields = ['subject', 'body', 'author_email']
