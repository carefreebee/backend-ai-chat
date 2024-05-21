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

class AIChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming each AI response is associated with a user
    content = models.TextField()  # Field to store the AI response content
    created_at = models.DateTimeField(auto_now_add=True)  # Field to store the timestamp when the AI response was created

    def __str__(self):
        return f'AIChat object (User: {self.user.username}, Content: {self.content[:50]}, Created: {self.created_at})'