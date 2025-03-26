from django import forms
from home.models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']  # 입력받을 필드를 정의