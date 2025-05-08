from django import forms
from .models import PostSkip, SkipComment

class PostSkipModelForm(forms.ModelForm):
    class Meta:
        model = PostSkip
        fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = SkipComment
        fields = ['comment']