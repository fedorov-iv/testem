from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from questionnaires.forms import QuestionnaireForm


@login_required
def index(request):
    return render(request, 'questionnaires/index.html')


@login_required
def create_test(request):

    success = False

    if request.method == 'POST':
        f = QuestionnaireForm(request.POST)
        if f.is_valid():
            success = True
            f.instance.is_active = False
            f.instance.author = request.user
            f.save()
    else:
        f = QuestionnaireForm()

    return render(request, 'questionnaires/create_test.html', {'form': f, 'success': success})
