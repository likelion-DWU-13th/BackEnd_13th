from django.contrib import admin
from django.urls import path
from yourpick import views

urlpatterns = [
    # path('', views.yourPick, name='yourpick'),
    path('yourpick_list/', views.yourpick_list, name="yourpick_list"),
    path('yourpick_detail/<int:yourpick_id>/', views.yourpick_detail, name="yourpick_detail"),
    path('yourpick_update/<int:id>/', views.yourpick_update, name="yourpick_update"),
    path('yourpick_delete/<int:id>/', views.yourpick_delete, name="yourpick_delete"),
]