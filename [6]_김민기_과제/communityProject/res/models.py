from django.db import models
from django.conf import settings

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
