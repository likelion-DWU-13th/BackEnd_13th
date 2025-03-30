from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(verbose_name="음악 제목", max_length=128)
    singer = models.CharField(verbose_name="가수 이름", max_length=128)
    body = models.TextField(verbose_name="리뷰 작성", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    def __str__(self):  #admin에서 글 제목을 표시
        return self.title