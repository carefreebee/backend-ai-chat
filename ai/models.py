from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chat(models.Model):
    chat = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'id': self.id,
            'chat': self.chat,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id,
        }