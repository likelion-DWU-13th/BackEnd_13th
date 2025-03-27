from django import forms
from .models import PostPick

class PostPickModelForm(forms.ModelForm):
    class Meta:
        model = PostPick
        fields = ['title', 'body']