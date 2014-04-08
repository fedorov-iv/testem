# -*- coding: utf8 -*-
from django.shortcuts import render, redirect
from feedback.forms import FeedbackForm
from mailtemplates.models import MailTemplate
from django.core.mail import EmailMessage
from django.contrib import messages


def index(request):

    if request.method == 'POST':

        f = FeedbackForm(user=request.user, data=request.POST)
        if f.is_valid():

            if request.user.is_authenticated():
                f.instance.user = request.user

            f.save()

            # отправляем письмо с данными учетной записи пользователю
            mail_template = MailTemplate.objects.get(code__exact='USERFEEDBACK')
            body = mail_template.body.replace('###hostname###', request.get_host())
            body = body.replace('###author_email###', f.instance.author_email)
            body = body.replace('###subject###', f.instance.subject)
            body = body.replace('###body###', f.instance.body)

            email = EmailMessage(
                mail_template.subject,
                body,
                mail_template.from_email,
                [mail_template.admin_email, ],
                mail_template.copy_emails.split(';'),
                headers={'Reply-To': mail_template.from_email, 'From': mail_template.from_name}
            )

            email.content_subtype = "html"
            email.send()
            messages.add_message(request, messages.SUCCESS, "Сообщение успешно отправлено!")
            return redirect('feedback_index')

    else:
        f = FeedbackForm()

    return render(request, 'feedback/index.html', {'form': f})
