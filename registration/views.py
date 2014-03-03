# -*- coding: utf8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.core.mail import EmailMessage
from mailtemplates.models import MailTemplate
from registration.forms import RegistrationForm


def index(request):

    success = False

    if request.method == 'POST':
        f = RegistrationForm(request.POST)
        if f.is_valid():
            success = True
            f.instance.is_active = False

            #print f.cleaned_data

            f.save()
            # присоединяем пользователя к группе зарегистрированных пользователей
            g = Group.objects.get(pk=1)
            f.instance.groups.add(g)
            # отправляем письмо с данными учетной записи пользователю
            mail_template = MailTemplate.objects.get(code__exact='USERREGISTRATION')
            body = mail_template.body.replace('###hostname###', request.get_host())
            body = body.replace('###username###', request.POST.get('username'))
            body = body.replace('###password###', request.POST.get('password'))
            body = body.replace('###activation_link###', 'http://' + request.get_host() + '/registration/activate/{0}/'.format(request.POST.get('username')))

            email = EmailMessage(
                mail_template.subject,
                body,
                mail_template.from_email,
                [request.POST.get('email').strip(), ],
                mail_template.copy_emails.split(';'),
                headers={'Reply-To': mail_template.from_email, 'From': mail_template.from_name}
            )

            email.content_subtype = "html"
            email.send()
            return redirect('registration_success')

    else:
        f = RegistrationForm()

    context = {'form': f.as_table(), 'success': success}
    return render(request, 'registration/index.html', context)


def success(request):
    context = {'success': True}
    return render(request, 'registration/index.html', context)


def activate(request, username):
        try:
            user = User.objects.get(username__exact=username)

        except(KeyError, User.DoesNotExist):
            context = {'not_found': True}
            return render(request, 'registration/activate.html', context)
        else:
            user.is_active = True
            user.save()
            context = {'not_found': False}
            return render(request, 'registration/activate.html', context)

