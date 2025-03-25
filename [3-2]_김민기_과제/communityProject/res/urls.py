from django.contrib import admin
from django.urls import path
from res import views

urlpatterns = [
    path("", views.resume, name="res"),
]