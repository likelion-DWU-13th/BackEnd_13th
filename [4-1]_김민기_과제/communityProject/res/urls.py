from django.contrib import admin
from django.urls import path
from res import views

urlpatterns = [
    path("", views.resume, name="res"),
    path("feedback_list/", views.feedback_list, name="feedback_list"), 
    path("feedback_detail/<int:page_id>/", views.feedback_detail, name="feedback_detail"),
    path("feedback_update/<int:id>/", views.feedback_update, name="feedback_update"),
    path("feedback_delete/<int:id>/", views.feedback_delete, name="feedback_delete"),

]