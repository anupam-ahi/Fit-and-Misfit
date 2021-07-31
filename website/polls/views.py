from django.http.response import HttpResponse
from django.shortcuts import render

from .models import *
from .forms import *
# Create your views here.


def home(request):
    return render(request, "home_beta_video.html")


def home_back(request):
    return render(request, "home_back.html")


def contact(request):
    return render(request, "contacts.html")


def recommendations(request):
    return render(request, "recommendations.html")


def newsletter(request):
    cont = {}
    i_form = email_form()
    cont['form'] = i_form

    if request.method == "POST":
        i_form = email_form(request.POST)
        if i_form.is_valid():

            email = i_form.cleaned_data['email']
            print(email)

    return render(request, "newsletter.html")


def books(request):
    return render(request, "books-beta.html")


def articles(request):
    return render(request, "articles-beta.html")


def audio_books(request):
    return render(request, "audio_books.html")
