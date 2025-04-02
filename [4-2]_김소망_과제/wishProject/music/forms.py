from django import forms
from .models import Music, Comment

class MusicModelForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title','singer', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']