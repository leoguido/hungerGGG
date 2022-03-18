from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('send/tributes/number/', views.tribute_forms, name = "tribute_forms")
]