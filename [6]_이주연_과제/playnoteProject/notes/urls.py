from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path("", views.create, name="create"),
    path("list/", views.list, name="list"),
    path("detail/<int:note_id>/", views.detail, name="detail"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),

    path("comment_create/<int:id>/", views.comment_create, name="comment_create"),
    path("comment_update/<int:note_id>/<int:com_id>/", views.comment_update, name="comment_update"),
    path("comment_delete/<int:note_id>/<int:com_id>/", views.comment_delete, name="comment_delete"),

    path("note/<int:note_id>/likes/", views.note_likes, name="note_likes"),
    path("comment/<int:com_id>/likes/", views.comment_likes, name="comment_likes"),

    path("note/<int:note_id>/scraps/", views.scraps, name="scraps"),
]