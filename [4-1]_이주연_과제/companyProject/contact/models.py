from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(verbose_name="이름", max_length = 20)
    email = models.EmailField(verbose_name="이메일", default="")
    subject = models.CharField(verbose_name="제목", max_length = 128)
    message = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    def __str__(self):
        return self.subject
