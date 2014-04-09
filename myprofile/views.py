# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from myprofile.forms import MyProfileForm
from django.shortcuts import redirect
from django.contrib import messages

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