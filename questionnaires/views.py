from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from questionnaires.forms import QuestionnaireForm
from questionnaires.models import Questionnaire, Question
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404


@login_required
def index(request, page=1):

    tests = Questionnaire.objects.filter(author=request.user)

    per_page = 5
    page_object = Paginator(tests, per_page)
    try:
        curr_page_tests = page_object.page(page)
    except EmptyPage:
        raise Http404()

    return render(request,
        'questionnaires/index.html',
        {

            'tests': curr_page_tests,
            'pages': page_object.page_range,
            'active_page': int(page),
            'pages_count':  page_object.num_pages
        })


@login_required
def create_test(request, questionnaire_id=0):

    questionnaire = None

    if questionnaire_id:
        #questionnaire = Questionnaire.objects.get(pk=questionnaire_id)
        questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id, author=request.user)

    if request.method == 'POST':

        f = QuestionnaireForm(request.POST, instance=questionnaire)
        if request.POST.get('delete'):
            return redirect(reverse('delete_test', args=[f.instance.id]))

        if f.is_valid():

            f.instance.author = request.user
            f.save()

            if request.POST.get('save'):
                return redirect(reverse("create_test", args=[f.instance.id]))

            if request.POST.get('exit'):
                return redirect(reverse("account"))

    else:
        if questionnaire:
            f = QuestionnaireForm(instance=questionnaire)
        else:
            f = QuestionnaireForm()

    return render(request, 'questionnaires/create_test.html', {'form': f})


@login_required
def delete_test(request, questionnaire_id=0):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id, author=request.user)
    questionnaire.delete()
    return redirect(reverse("account"))


@login_required
def create_questions(request, questionnaire_id=0):
    return render(request, 'questionnaires/create_questions.html', {'questionnaire_id': questionnaire_id})