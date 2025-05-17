from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import GuestViewSet, CommentViewSet

guest_router = SimpleRouter(trailing_slash=False)
guest_router.register('guests', GuestViewSet, basename='guest')

comment_router = SimpleRouter(trailing_slash=False)
comment_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(guest_router.urls)),
    path('guests/<int:guest_id>/', include(comment_router.urls)),

]