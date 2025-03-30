from django import forms
from .models import Music

class MusicModelForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title','singer', 'body']