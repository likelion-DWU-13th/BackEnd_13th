from django.contrib import admin
from django.urls import path
from contact import views

urlpatterns = [
    path("", views.submitContact, name="contact"),
    path("contact_list/", views.contact_list, name="contact_list"),
    path("contact_detail/<int:id>/", views.contact_detail, name="contact_detail"),
    path("contact_edit/<int:id>/", views.contact_edit, name="contact_edit"),
    path("contact_delete/<int:id>/", views.contact_delete, name="contact_delete"),

    path("create_comment/<int:contact_id>/", views.create_comment, name="create_comment"),
    path("update_comment/<int:contact_id>/<int:comment_id>/", views.update_comment, name="update_comment"),
    path("delete_comment/<int:contact_id>/<int:comment_id>/", views.delete_comment, name="delete_comment"),
]