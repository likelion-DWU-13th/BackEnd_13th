from django.contrib import admin
from django.urls import path
from contact import views

urlpatterns = [
    path("", views.submitContact, name="contact"),
    path("contact_list/", views.contact_list, name="contact_list"),
    path("contact_detail/<int:id>/", views.contact_detail, name="contact_detail"),
    path("contact_edit/<int:id>/", views.contact_edit, name="contact_edit"),
    path("contact_delete/<int:id>/", views.contact_delete, name="contact_delete")
]