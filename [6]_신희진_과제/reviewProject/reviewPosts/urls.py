from django.contrib import admin
from django.urls import path
from reviewPosts import views

urlpatterns = [
    path ("", views.reviewPost, name = "reviewPosts"),
    path("review_list/", views.review_list, name="review_list"),
]
