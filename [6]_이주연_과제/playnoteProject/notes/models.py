from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# 게시글 작성 모델
class Note(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='notes-img')

    like_users=models.ManyToManyField(User, related_name='like_notes')
    scrap_users=models.ManyToManyField(User, related_name='scrap_notes')
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

# 댓글 작성 모델
class Comment(models.Model):
    comment = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, upload_to='comment-photo')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like_users=models.ManyToManyField(User, related_name='like_comments')

    def __str__(self):
        return self.comment