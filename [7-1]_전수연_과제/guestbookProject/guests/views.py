from django.shortcuts import render
from .models import Guest, Comment
from .serializers import GuestSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

    def get_queryset(self, **kwargs):
        id = self.kwargs['guest_id']
        return self.queryset.filter(guest=id)

