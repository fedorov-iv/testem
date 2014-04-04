# -*- coding: utf8 -*-
from django.shortcuts import render, redirect
from feedback.forms import FeedbackForm
from mailtemplates.models import MailTemplate
from django.core.mail import EmailMessage


def index(request):
    success = False

    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            success = True

            #print f.cleaned_data

            f.save()

            # отправляем письмо с данными учетной записи пользователю
            mail_template = MailTemplate.objects.get(code__exact='USERFEEDBACK')
            body = mail_template.body.replace('###hostname###', request.get_host())
            body = body.replace('###email###', request.POST.get('email'))
            body = body.replace('###subject###', request.POST.get('subject'))
            body = body.replace('###body###', request.POST.get('body'))

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
            return redirect('feedback_index')

    else:
        f = FeedbackForm()

    context = {'form': f, 'success': success}
    return render(request, 'registration/index.html', context)
