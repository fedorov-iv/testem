# -*- coding: utf8 -*-
from django.contrib.auth.models import User, Group
from django import forms


class RegistrationForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'username', 'email', 'password']
            widgets = {
                'password': forms.PasswordInput,
            }

        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['first_name'] = forms.CharField(label=u"Имя", required=True)
            self.fields['last_name'] = forms.CharField(label=u"Фамилия", required=True)
            self.fields['email'] = forms.EmailField(label=u"E-mail", required=True)

        #пост-обработка данных формы с валидацией (оставил здесь, т.к. очень удобно в ряде случаев)
        def clean_username(self):
            form_username = self.cleaned_data.get('username')
            try:
                User.objects.filter(username=form_username)
            except User.DoesNotExist:
                return form_username
            raise forms.ValidationError("Такое имя пользователя уже существует")


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