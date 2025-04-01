from django.urls import path
from .views import *

urlpatterns = [
    path('', post, name='post'),

    path('post_list', post_list, name='post_list'), 
    path('post_detail/<int:post_id>/', post_detail, name='post_detail'),
    path('post_update/<int:id>/', post_update, name='post_update'),
    path('post_delete/<int:id>/', post_delete, name='post_delete'),

    path('create_comment/<int:id>/', create_comment, name='create_comment'),
    path('update_comment/<int:post_id>/<int:com_id>/', update_comment, name='update_comment'),
    path('delete_comment/<int:post_id>/<int:com_id>/', delete_comment, name='delete_comment'),
]