from django.contrib import admin
from django.urls import path
from music import views

urlpatterns = [
    path("", views.music, name="music"),
    path('create/', views.create, name='create'),  # 리뷰 작성 기능
    path("music_list/", views.music_list, name="music_list"),
    path("music_detail/<int:music_id>/", views.music_detail, name="music_detail"),
    path("music_update/<int:id>/", views.music_update, name="music_update"),
    path("music_delete/<int:id>/", views.music_delete, name="music_delete"),
]