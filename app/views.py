from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from app.models import QUESTIONS




# Create your views here.


def index(request):

    context = {'questions': QUESTIONS, 'is_auth': True,'page_obj':listing(request,QUESTIONS)}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    question_item = QUESTIONS[question_id]
    context = {'question': question_item, 'is_auth': True,'page_obj':listing(request,QUESTIONS)}
    return render(request, 'question.html', context=context)


def hot(request):
    context = {'questions': QUESTIONS, 'is_auth': True,'page_obj':listing(request,QUESTIONS)}
    return render(request, 'hot.html', context=context)


def tag(request):
    context = {'questions': QUESTIONS, 'is_auth': True,'page_obj':listing(request,QUESTIONS)}
    return render(request, 'tag-index.html', context=context)


def login(request):
    context = {'questions': QUESTIONS, 'is_auth': False}
    return render(request, 'login.html', context=context)


def ask(request):
    context = {'questions': QUESTIONS, 'is_auth': True}
    return render(request, 'ask.html', context=context)


def signup(request):
    context = {'questions': QUESTIONS, 'is_auth': False}
    return render(request, 'sign-up.html', context=context)


def settings(request):
    context = {'questions': QUESTIONS, 'is_auth': True}
    return render(request, 'settings.html', context=context)

def listing(request, pagList):
    contact_list = pagList
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
