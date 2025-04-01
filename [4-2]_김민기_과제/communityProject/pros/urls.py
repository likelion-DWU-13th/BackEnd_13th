from django.contrib import admin
from django.urls import path
from pros import views

urlpatterns = [
    path("", views.project, name="pros"),
]