from django import forms
from .models import Page

class PageModelForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'body']