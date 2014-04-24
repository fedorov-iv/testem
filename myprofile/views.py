# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from myprofile.forms import MyProfileForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

@login_required
def index(request):

    if request.method == 'POST':
        f = MyProfileForm(request.POST, instance=request.user)
        if f.is_valid():
            f.save()

            messages.add_message(request, messages.SUCCESS, "Изменения успешно сохранены!")
            return redirect('user_profile')

    else:
        f = MyProfileForm(instance=request.user)

    return render(request, "myprofile/user_profile.html", {'form': f})

@login_required
def change_password(request):

    if request.method == 'POST':
        request.user.set_password(request.POST.get('password'))
        request.user.save()
        messages.add_message(request, messages.SUCCESS, "Пароль успешно изменен!")

    return redirect(reverse('user_profile'))