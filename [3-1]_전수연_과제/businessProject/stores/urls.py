from django.contrib import admin
from django.urls import path, include
from stores import views

urlpatterns = [
    path('', views.stores, name='stores'),
]