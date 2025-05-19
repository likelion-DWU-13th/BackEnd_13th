from rest_framework.serializers import ModelSerializer # 1
from .models import Post, Comment # 직렬화에 사용할 모델 임포트 
from rest_framework import serializers
from django.contrib.auth.models import User

class PostSerializer(ModelSerializer): # 2
    writer = serializers.ReadOnlyField(source = 'writer.username')
    
    class Meta:
        model = Post # 직렬화에 사용할 모델
        fields = [ 'id', 'title', 'content', 'writer' ] # 직렬화 할 필드

class CommentSerializer(ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.username')
    class Meta:
        model = Comment
        fields = [ 'id', 'comment', 'post', 'writer' ] 