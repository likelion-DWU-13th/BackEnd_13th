from django.contrib import admin
from django.urls import path
from picks import views

urlpatterns = [
    path("", views.pick, name="picks"),
    path("create_pick/", views.create, name='create_pick'),
]