from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home_back, name="home_back"),

    # path('home', views.home, name="home"),
    path('contact1', views.contact, name="contact"),
    # path('index', views.contact, name="index"),
    path('recommendations', views.recommendations, name="recommendations"),
    path('newsletter', views.newsletter, name="newsletter"),
    path('books-beta', views.books, name="books"),
    path('articles-beta', views.articles, name="articles"),
    path('audio_books', views.audio_books, name="audio_books"),
]
