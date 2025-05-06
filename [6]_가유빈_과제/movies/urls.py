from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('', views.my_bookmarks, name="movies"),
    path('bookmark/<int:review_id>/', views.toggle_bookmark, name='toggle_bookmark'),
    path('bookmarks/', views.my_bookmarks, name='bookmark_list'),
]