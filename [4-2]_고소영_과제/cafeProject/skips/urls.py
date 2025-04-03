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
    path('skip_create_comment/<int:id>/', views.skip_create_comment, name='skip_create_comment'),
    path('skip_update_comment/<int:skip_id>/<int:com_id>/', views.skip_update_comment, name='skip_update_comment'),
    path('skip_delete_comment/<int:skip_id>/<int:com_id>/', views.skip_delete_comment, name='skip_delete_comment'),
]