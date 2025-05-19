from rest_framework.routers import SimpleRouter # 1
from django.urls import path, include
from .views import PostViewSet, CommentViewSet


post_router = SimpleRouter(trailing_slash=False) # 2
post_router.register('posts', PostViewSet, basename='post') # 3

comment_router = SimpleRouter(trailing_slash=False)
comment_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(post_router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls)),
]