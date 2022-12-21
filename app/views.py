from django.contrib.auth.context_processors import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from . import models
from .forms import LoginForm, RegistrationForm, AskForm


def loged(request):
    context = {'questions': models.Question, 'tags': models.Tag}
    return render(request, 'index.html', context=context)


def mainpage(request):
    contact_list = models.Question.objects.get_new_questions()
    context = {'questions': models.Question, 'tags': models.Tag,
               'page_obj': pagging(contact_list, request), 'profiles': models.Profile, 'likes': models.LikeQuestion}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    contact_list = models.Answer.objects.get_answers(question_id)
    context = {'question': models.Question.objects.find_by_id(question_id), 'answers': models.Answer,
               'tags': models.Tag,
               'page_obj': pagging(contact_list, request)}
    return render(request, 'question.html', context=context)


def tagpage(request, tag_id: int):
    contact_list = models.Question.objects.get_tagged_questions(tag_id)
    context = {'questions': models.Question, 'tags': models.Tag, 'tag': models.Tag.objects.find_by_id(tag_id),
               'page_obj': pagging(contact_list, request)}
    return render(request, 'tag-index.html', context=context)


def hot(request):
    contact_list = models.Question.objects.get_hot_questions()
    context = {'questions': models.Question, 'tags': models.Tag, 'page_obj': pagging(contact_list, request)}
    return render(request, 'hot.html', context=context)


def settings(request):
    context = {'tags': models.Tag}
    return render(request, 'settings.html', context=context)


def login(request):
    if request.method == 'GET':
        user_form=LoginForm()
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            user = authenticate(request=request,**user_form.cleaned_data)
            if user:
                return redirect(reverse("index"))
            else:
                user_form.add_error(field=None,error="Wrong Username")
    return render(request, "login.html", {'form':user_form})


def signup(request):
    if request.method == 'GET':
        user_form = RegistrationForm()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user:
                return redirect(reverse("index"))
            else:
                user_form.add_error(field=None, error="User Saving error")
    return render(request, 'sign-up.html', {'form':user_form})


def ask(request):
    if request.method == 'GET':
        ask_form = AskForm()
    if request.method == 'POST':
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            ask = ask_form.save()
            if ask:
                return redirect(reverse("index"))
    return render(request, 'ask.html', {'form': ask_form})


def pagging(contact_list, request):
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        page = int(page_number)
        if page > paginator.num_pages: raise Http404
    except ValueError:
        return HttpResponseBadRequest()
    return paginator.get_page(page_number)


def likes(question_like, answer_like):
    likes_count = {'questions': models.LikeQuestion.objects.get_questions_likes(question_like),
                   'answers': models.LikeAnswer.objects.get_answers_likes(answer_like)}
    return likes_count
