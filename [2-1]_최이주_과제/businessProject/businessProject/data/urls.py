from django.contrib import admin
from django.urls import path
from data import views

urlpatterns = [
    path("", views.data, name="data"),
]

