from django.contrib import admin
from django.urls import path
from skips import views

urlpatterns = [
    path("", views.skip, name="skips"),
    path("create_skip/", views.create, name="create_skip"),
]