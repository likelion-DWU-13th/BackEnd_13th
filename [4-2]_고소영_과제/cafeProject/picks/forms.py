from django import forms
from .models import PostPick, Comment

class PostPickModelForm(forms.ModelForm):
    class Meta:
        model = PostPick
        fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']