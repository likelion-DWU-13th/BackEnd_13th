from django.contrib import admin
from django.urls import path
from reviews import views

urlpatterns = [
    path('', views.reviews, name='reviews'), #리뷰 목록록
    path('create/', views.create, name='create'), #영화 리뷰 작성
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'), #리뷰 상세
    path("review_update/<int:id>/", views.review_update, name="review_update"), #리뷰 수정
    path("review_delete/<int:id>/", views.review_delete, name="review_delete"), #리뷰 삭제

    path('create_comment/<int:id>/', views.create_comment, name='create_comment'),
    path('update_comment/<int:review_id>/<int:com_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:review_id>/<int:com_id>/', views.delete_comment, name='delete_comment'),

    path('<int:review_id>/likes/', views.likes, name='likes'), #좋아요
]