from django.contrib import admin
from django.urls import path
from music import views

urlpatterns = [
    path("", views.music, name="music"),
    path('create/', views.create, name='create'),  # 리뷰 작성 기능
]