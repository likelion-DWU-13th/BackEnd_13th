from django.contrib import admin
from django.urls import path
from home import views 
from yourpick import views as yourpick_views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend/', views.recommend, name='recommend'),
    path('yourpick/', yourpick_views.yourpick_list, name='yourpick')
]
