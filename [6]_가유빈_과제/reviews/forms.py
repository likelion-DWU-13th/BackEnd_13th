from django import forms
from .models import Review, Comment

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']