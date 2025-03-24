from django.contrib import admin
from django.urls import path
from datas import views

urlpatterns = [
    path("", views.data, name="data"),
]

