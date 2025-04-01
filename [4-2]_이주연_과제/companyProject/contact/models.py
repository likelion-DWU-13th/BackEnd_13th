from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(verbose_name="이름", max_length = 20)
    email = models.EmailField(verbose_name="이메일", default="")
    subject = models.CharField(verbose_name="제목", max_length = 128)
    message = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='contact_photo')

    def __str__(self):
        return self.subject

class Comment(models.Model):
    comment = models.CharField(max_length=350)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(ContactMessage, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment
