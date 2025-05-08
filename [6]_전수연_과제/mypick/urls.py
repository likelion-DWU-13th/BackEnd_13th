from django.contrib import admin
from django.urls import path
from mypick import views

urlpatterns = [
    path('', views.myPick, name='mypick'),
]