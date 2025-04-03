from django.contrib import admin
from django.urls import path
from picks import views

urlpatterns = [
    path("", views.pick, name="picks"),
    path("create_pick/", views.create, name='create_pick'),
    path("pick_list/", views.pick_list, name="pick_list"),
    path("pick_detail/<int:id>/", views.pick_detail, name="pick_detail"),
    path("pick_update/<int:id>/", views.pick_update, name="pick_update"),
    path("pick_delete/<int:id>/", views.pick_delete, name="pick_delete"),
    path('create_comment/<int:id>/', views.create_comment, name='create_comment'),
    path('update_comment/<int:pick_id>/<int:com_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:pick_id>/<int:com_id>/', views.delete_comment, name='delete_comment'),
]