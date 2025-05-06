from django import forms
from .models import Page, Comment

class PageModelForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']