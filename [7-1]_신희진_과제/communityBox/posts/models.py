from django.db import models
from django.contrib.auth.models import User # 추가

# Create your models here.
class Post(models.Model) : 
    title = models.CharField(verbose_name="제목", max_length=128)
    content = models.TextField(verbose_name="내용", default='') 
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    # 추가) 게시글 작성자 
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment = models.CharField(verbose_name="댓글", max_length=128)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # 추가) 댓글 작성자 
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.comment