from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=128)
    artist = models.CharField(verbose_name='아티스트', max_length=128)
    body = models.TextField(verbose_name='소개', default='')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"
