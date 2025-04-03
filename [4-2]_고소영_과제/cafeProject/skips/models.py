from django.db import models

# Create your models here.
class PostSkip(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="이유", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지",
                              blank=True, null=True, upload_to='skip_photo')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(PostSkip, on_delete=models.CASCADE,
                                related_name='comments')
    def __str__(self):
        return self.comment