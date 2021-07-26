from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def recommendations(request):
    return render(request, "recommendations.html")


def newsletter(request):
    return render(request, "newsletter.html")


def books(request):
    return render(request, "books.html")


def articles(request):
    return render(request, "articles.html")


def audio_books(request):
    return render(request, "audio_books.html")
