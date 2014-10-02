# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from questionnaires.forms import QuestionnaireForm, QuestionForm
from questionnaires.models import Questionnaire, Question, AnswerVariant, UserAnswer
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404, HttpResponse
from django.core import serializers
import json
from django.contrib import messages
import datetime


#  список "моих" тестов
@login_required
def index(request):
    return render(request, 'questionnaires/index.html')


#  Данные, получаемые через ajax  для списка "моих" тестов
@login_required
@csrf_exempt
def index_data(request):

    sort = request.POST.getlist("sort")

    print sort
    current = request.POST.get("current", 1)
    total = Questionnaire.objects.filter(author=request.user).count()
    row_count = request.POST.get("rowCount", 10)
    questionnaires = Questionnaire.objects.filter(author=request.user)

    page_object = Paginator(questionnaires, row_count)
    try:
        curr_page_questionnaires = page_object.page(current)
    except EmptyPage:
        raise Http404()

    rows = []
    for questionnaire in curr_page_questionnaires:
        rows.append({"id": questionnaire.id,
                     "title": questionnaire.title,
                     "is_active": questionnaire.is_active,
                     "questions": questionnaire.question_set.all().count(),
                     "create_date": "{0:02d}.{1:02d}.{2}".format(questionnaire.create_date.day, questionnaire.create_date.month, questionnaire.create_date.year),
                     "description": questionnaire.description}
        )

    ajax_response = {"current": current, "rowCount": row_count, "rows": rows, "total": total}
    return HttpResponse(json.dumps(ajax_response), content_type="application/json; charset=utf8")


#  создание теста
@login_required
def create_test(request, questionnaire_id=0):
    questionnaire = None

    if questionnaire_id:
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


#  тест (подробно) для заполнения
def questionnaire_detail(request, questionnaire_id=0):
    if request.method == 'POST':  # валидация и сохранение ответов
        questionnaire = get_object_or_404(Questionnaire, pk=request.POST.get("t"))

        # print request.POST
        chosen_variants = [int(key.split("_")[1]) for key in request.POST.keys() if key.startswith("v")]  # выбранные варианты
        user_score = 0  # сумма баллов, набираемая пользователем в тесте

        for chv in chosen_variants:
            try:
                av = AnswerVariant.objects.get(pk=chv)
            except AnswerVariant.DoesNotExist:
                continue

            user_score += av.weight

        # сохраняем результат в базу
        ua = UserAnswer()
        ua.author = request.user
        ua.title = u'Результат теста "{0}"'.format(questionnaire.title)
        ua.create_date = datetime.datetime.now()
        ua.questionnaire = questionnaire
        ua.test_score = 0
        ua.user_score = user_score
        ua.save()

        return redirect(reverse('questionnaire_success', args=[ua.id]))

    else:  # загрузка теста для заполнения
        questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
        questions = Question.objects.filter(questionnaire=questionnaire)
        return render(request, 'questionnaires/detail.html', {'questionnaire': questionnaire, 'questions': questions})


def questionnaire_success(request, user_answer_id=0):
    user_answer = get_object_or_404(UserAnswer, pk=user_answer_id)
    return render(request, 'questionnaires/success.html', {'user_answer':user_answer})