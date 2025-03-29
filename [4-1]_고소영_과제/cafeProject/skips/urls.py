from django.contrib import admin
from django.urls import path
from skips import views

urlpatterns = [
    path("", views.skip, name="skips"),
    path("create_skip/", views.create, name="create_skip"),
    path("skip_list/", views.skip_list, name="skip_list"),
    path("skip_detail/<int:id>/", views.skip_detail, name="skip_detail"),
    path("skip_update/<int:id>/", views.skip_update, name="skip_update"),
    path("skip_delete/<int:id>/", views.skip_delete, name="skip_delete"),
]