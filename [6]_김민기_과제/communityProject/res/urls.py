from django.contrib import admin
from django.urls import path
from res import views

urlpatterns = [
    path("", views.resume, name="res"),
    path("feedback_list/", views.feedback_list, name="feedback_list"), 
    path("feedback_detail/<int:page_id>/", views.feedback_detail, name="feedback_detail"),
    path("feedback_update/<int:id>/", views.feedback_update, name="feedback_update"),
    path("feedback_delete/<int:id>/", views.feedback_delete, name="feedback_delete"),
    path('likes/<int:like_id>/toggle/', views.like_toggle, name='like_toggle'),

    path('create_comment/<int:id>/', views.create_comment, name='create_comment'),
    path('update_comment/<int:page_id>/<int:com_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:page_id>/<int:com_id>/', views.delete_comment, name='delete_comment'),

]