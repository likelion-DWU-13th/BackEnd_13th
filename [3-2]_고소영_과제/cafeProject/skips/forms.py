from django import forms
from .models import PostSkip

class PostSkipModelForm(forms.ModelForm):
    class Meta:
        model = PostSkip
        fields = ['title', 'body']