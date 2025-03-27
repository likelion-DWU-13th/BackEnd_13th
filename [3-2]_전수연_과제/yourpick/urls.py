from django.contrib import admin
from django.urls import path
from yourpick import views

urlpatterns = [
    path('', views.yourPick, name='yourpick'),
]