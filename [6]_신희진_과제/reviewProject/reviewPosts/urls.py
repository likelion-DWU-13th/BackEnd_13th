from django.contrib import admin
from django.urls import path
from reviewPosts import views

urlpatterns = [
    path ("", views.review_list, name = "review_list"),
    path("review_detail/<int:post_id>/", views.review_detail, name="review_detail"), # post.id 여야지만 작동. 왜?
    path("review_update/<int:id>/", views.review_update, name="review_update"),
    path("review_delete/<int:id>/", views.review_delete, name="review_delete"),

    path('create_comment/<int:id>/', views.create_comment, name='create_comment'),
    path('update_comment/<int:post_id>/<int:com_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:post_id>/<int:com_id>/', views.delete_comment, name='delete_comment'),
]