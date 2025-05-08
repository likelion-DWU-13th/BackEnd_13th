from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostPick(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="이유", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", 
                              blank=True, null=True, upload_to='pick_photo')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='liked_picks', blank=True)

    def __str__(self):
        return self.title
    
class PickComment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(PostPick, on_delete=models.CASCADE,
                                related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.comment