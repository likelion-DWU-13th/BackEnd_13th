from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

DELAY_CHOICES = [
    ('now', '지금'),
    ('1d', '1일 후'),
    ('7d', '7일 후'),
    ('30d', '30일 후'),
    ('365d', '1년 후'),
]
class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=200)
    body = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='letter_photo')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    delay_choice = models.CharField(max_length=5, choices=DELAY_CHOICES, default='1d')

    def get_visible_time(self):
        days = int(self.delay_choice.replace('d', ''))
        return self.created_at + timedelta(days=days)

    def is_visible(self):
        if self.delay_choice == 'now':
            return True
        return timezone.now() >= self.get_visible_time()
    
    def __str__(self):
        return self.title
# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment