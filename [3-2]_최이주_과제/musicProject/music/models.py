from django.db import models

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('k-pop', 'K-POP'),
        ('R&B', 'R&B'),
        ('hiphop', '힙합'),
        ('pop', '팝'),
        ('rock', '락'),
        ('jazz', '재즈'),
        ('etc', '기타'),
    ]
    title = models.CharField(verbose_name="노래", max_length=128)
    singer = models.CharField(verbose_name="가수", max_length=64, default="Unknown")
    category = models.CharField(verbose_name="장르", max_length=10, choices=CATEGORY_CHOICES, default='etc')
    body = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    def __str__(self):
        return self.title