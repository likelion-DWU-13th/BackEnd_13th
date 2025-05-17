from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Guest, Comment
from django.contrib.auth.models import User

class GuestSerializer(ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.username')

    class Meta:
        model = Guest
        fields = ['id', 'name', 'content', 'writer']

class CommentSerializer(ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.username')

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'guest', 'writer']
