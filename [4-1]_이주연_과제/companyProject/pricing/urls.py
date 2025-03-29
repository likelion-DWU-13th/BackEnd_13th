from django.contrib import admin
from django.urls import path
from pricing import views

urlpatterns = [
    path("", views.pricing, name="pricing")
]