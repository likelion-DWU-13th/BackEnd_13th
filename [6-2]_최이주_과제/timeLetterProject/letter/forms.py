from django import forms
from .models import Post, Comment

class letterModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'photo', 'delay_choice']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']