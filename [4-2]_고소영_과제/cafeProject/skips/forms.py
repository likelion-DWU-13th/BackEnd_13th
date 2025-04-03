from django import forms
from .models import PostSkip, Comment

class PostSkipModelForm(forms.ModelForm):
    class Meta:
        model = PostSkip
        fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']