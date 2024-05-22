from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Chat(models.Model):
    chat = models.TextField(null=True)
    user = models.ForeignKey(User, related_name='chats', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

 

class GroupChat(models.Model):
    users = models.ManyToManyField(User, related_name='group_chats')
    chats = models.ManyToManyField(Chat, related_name='group_chats')
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='groupchat_creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class PrivateChat(models.Model):
    user1 = models.ForeignKey(User, related_name='private_chats_1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='private_chats_2', on_delete=models.CASCADE)
    chats = models.ManyToManyField(Chat, related_name='private_chats')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)