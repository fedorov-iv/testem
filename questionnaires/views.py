# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from questionnaires.forms import QuestionnaireForm, QuestionForm
from questionnaires.models import Questionnaire, Question, AnswerVariant
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404, HttpResponse
from django.core import serializers
from django.contrib import messages


#  список "моих" тестов
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
                      'pages_count': page_object.num_pages
                  })


#  создание теста
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

            messages.add_message(request, messages.SUCCESS, "Изменения успешно сохранены!")

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


#  удаление теста
@login_required
def delete_test(request, questionnaire_id=0):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id, author=request.user)
    questionnaire.delete()
    return redirect(reverse("account"))


#  получение деталей вопроса "моего" теста
@login_required
def get_question_details(request, question_id=0):
    question = get_object_or_404(Question, pk=question_id, author=request.user)
    answer_variants = question.answervariant_set.all()
    merged_data = list([question]) + list(answer_variants)
    return HttpResponse(serializers.serialize('json', merged_data, indent=5), content_type="application/json")


#  создание вопросов "моего" теста
@login_required
def create_questions(request, questionnaire_id=0):
    f = QuestionForm()

    if request.method == 'POST':
        questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id, author=request.user)

        question = None

        if request.POST.get("id"):
            question = get_object_or_404(Question, pk=request.POST.get("id"), author=request.user)

        f = QuestionForm(request.POST, instance=question)

        #print request.POST.getlist('q_id')

        if f.is_valid():
            f.instance.questionnaire = questionnaire
            f.instance.author = request.user
            f.save()
            # saving existing answer variants' values
            if request.POST.get('q_id'):
                for question_id in request.POST.getlist('q_id'):

                    av = get_object_or_404(AnswerVariant, pk=question_id, author=request.user, question=f.instance)
                    # if delete checkbox is set - delete answer variant
                    if request.POST.get('q_delete_' + question_id):
                        av.delete()
                        continue
                    #av.question = f.instance
                    #av.author = request.user
                    av.title = request.POST.get('q_title_' + question_id)
                    av.weight = request.POST.get('q_weight_' + question_id) if request.POST.get(
                        'q_weight_' + question_id) else 0
                    av.is_correct = True if request.POST.get('q_is_correct_' + question_id) else False
                    av.save()

            # saving new answer variants' values
            if request.POST.get('nq_id'):
                for question_id in request.POST.getlist('nq_id'):

                    # if title of answer variant is absent - delete answer variant
                    if not request.POST.get('nq_title_' + question_id):
                        continue
                    av = AnswerVariant()
                    av.question = f.instance
                    av.author = request.user
                    av.title = request.POST.get('nq_title_' + question_id)
                    av.weight = request.POST.get('nq_weight_' + question_id) if request.POST.get(
                        'nq_weight_' + question_id) else 0
                    av.is_correct = True if request.POST.get('nq_is_correct_' + question_id) else False
                    av.save()

            messages.add_message(request, messages.SUCCESS, "Изменения успешно сохранены!")
            return redirect(reverse('create_questions', args=[questionnaire.id]))

    questions = Question.objects.filter(questionnaire=questionnaire_id)
    return render(request,
                  'questionnaires/create_questions.html',
                  {'questionnaire_id': questionnaire_id, 'questions': questions, 'nform': f})


#  удаление вопроса "моего" теста
@login_required
def delete_question(request, question_id=0):
    question = get_object_or_404(Question, pk=question_id, author=request.user)
    question.delete()
    return redirect(reverse('create_questions', args=[question.questionnaire.id]))


#  список тестов для заполнения
def questionnaires_list(request, page=1):
    tests = Questionnaire.objects.filter(is_active=True).order_by("-create_date")

    per_page = 5
    page_object = Paginator(tests, per_page)
    try:
        curr_page_tests = page_object.page(page)
    except EmptyPage:
        raise Http404()

    return render(request,
                  'questionnaires/list.html',
                  {

                      'tests': curr_page_tests,
                      'pages': page_object.page_range,
                      'active_page': int(page),
                      'pages_count': page_object.num_pages
                  })