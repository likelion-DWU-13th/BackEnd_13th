from django.db import models
from django.contrib.auth.models import User
from reviews.models import Review # 다른 앱의 모델 import

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'review')  # 중복 북마크 방지
