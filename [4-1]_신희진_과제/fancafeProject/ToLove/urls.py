from django.contrib import admin
from django.urls import path
from ToLove import views

urlpatterns = [
    path("", views.toL, name = "toL"),
    path("toL_list/", views.toL_list, name = "toL_list"),
    path("toL_detail/<int:letter_id>/", views.toL_detail, name = "toL_detail"),
    path("toL_update/<int:id>/", views.toL_update, name = "toL_update"),
    path("toL_delete/<int:id>/", views.toL_delete, name = "toL_delete"),
]