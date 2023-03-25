from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index_without_template(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '<br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index_without_import_render(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def index_with_render(request):
    """we no longer need to import loader and HttpResponse (не нуждаемся в импорте loader и HttpResponse)
    выводит последние 5 вопросов по дате"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def index(request):
    """список с фильтром и исключение 404"""
    question_list = get_list_or_404(Question, pub_date__year__gte = 2022)  # год больше или равно 2022
    #question_list = get_list_or_404(Question, id=2)  - так тоже работает, но выведет одну позицию в списке
    return render(request, 'polls/index.html', {'latest_question_list': question_list})

def detail_without_template(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def detail_raise_Http404(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)