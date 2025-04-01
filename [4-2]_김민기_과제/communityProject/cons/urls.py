from django.contrib import admin
from django.urls import path
from cons import views

urlpatterns = [
    path("", views.contact, name="cons"),
]