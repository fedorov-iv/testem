# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from django import forms


class MyProfileForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email']

        def __init__(self, *args, **kwargs):
            super(MyProfileForm, self).__init__(*args, **kwargs)
            self.fields['first_name'] = forms.CharField(label=u"Имя", required=True)
            self.fields['last_name'] = forms.CharField(label=u"Фамилия", required=True)
            self.fields['email'] = forms.EmailField(label=u"E-mail", required=True)


        #def clean_first_name(self):
            #form_first_name = self.cleaned_data.get('first_name')
            #if form_first_name == '':
                #raise forms.ValidationError("Это поле обязательно для заполнения.")
            #return form_first_name

        #def clean_last_name(self):
            #form_last_name = self.cleaned_data.get('last_name')
            #if form_last_name == '':
                #raise forms.ValidationError("Это поле обязательно для заполнения.")
            #return form_last_name