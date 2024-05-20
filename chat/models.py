from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Chat(models.Model):
    chat = models.TextField(null=True)
    user = models.ForeignKey(User, related_name='chats', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

 
