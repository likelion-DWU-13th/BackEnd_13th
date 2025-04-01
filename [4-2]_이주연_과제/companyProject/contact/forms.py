from django import forms
from .models import ContactMessage, Comment

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comment']