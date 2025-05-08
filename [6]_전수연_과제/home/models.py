from django.db import models
from django.contrib.auth.models import User
import re
from urllib.parse import urlparse, parse_qs

class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=128)
    artist = models.CharField(verbose_name='아티스트', max_length=128)
    link = models.URLField(verbose_name='유튜브링크', max_length=300, null=True, blank=True)
    body = models.TextField(verbose_name='소개', default='')
    photo = models.ImageField(verbose_name="사진",
                              blank=True, null=True, upload_to='yourpick_photo')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"
    
    # 유튜브 링크에서 영상 ID를 추출합니다
    def get_youtube_id(self):
        if not self.link:
            return None
        match = re.search(r'(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|shorts/))([\w-]{11})', self.link)
        return match.group(1) if match else None

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Post, on_delete=models.CASCADE,
                                related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.comment
