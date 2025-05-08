from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'artist','link', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        