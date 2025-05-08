from django import forms
from .models import PostPick, PickComment

class PostPickModelForm(forms.ModelForm):
    class Meta:
        model = PostPick
        fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = PickComment
        fields = ['comment']