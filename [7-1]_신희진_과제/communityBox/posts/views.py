from django.shortcuts import render
from .models import Post, Comment # 1 
from .serializers import PostSerializer, CommentSerializer 
from rest_framework.viewsets import ModelViewSet # 2

class PostViewSet(ModelViewSet): # 3
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

    def get_queryset(self, **kwargs): # Override, 4
        id = self.kwargs['post_id']
        return self.queryset.filter(post=id)
