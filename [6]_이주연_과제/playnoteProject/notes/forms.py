from django import forms
from .models import Note, Comment
from django.forms import TextInput, Textarea

# 글 작성 폼
class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields=['title', 'content', 'image']
        widgets = {
            'title':TextInput(attrs={
                'class':'form-input', 'placeholder':'제목을 입력해주세요'
            }),
            'content':Textarea(attrs={
                'class':'form-textarea', 'placeholder':'정보를 공유해주세요!'
            })
        }

#댓글 작성 폼
class CommentModelFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comment', 'photo']
        widgets = {
            'comment':Textarea(attrs={
                'class':'form-textarea comment-textarea', 'placeholder': '댓글을 입력해주세요!'
            })
        }