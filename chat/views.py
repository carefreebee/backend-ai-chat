import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .models import Chat
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
# Create your views here.

@csrf_exempt
def addChat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        userId = data.get('userId')
        print('data', data, userId)
        
        try:
            user = User.objects.get(id=userId)
            print(user)
            
            chat = Chat.objects.create(chat=data.get('chat'), user=user)
            chat.save()
            return JsonResponse({'success': True})
        
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'User does not exist!'})
    

@csrf_exempt
def getChats(request):
    if request.method == 'GET':
  
        users_with_chats = Chat.objects.select_related('user').prefetch_related( Prefetch('user', queryset=User.objects.all()))
        # for chat in users_with_chats:
        #     print(f"Chat content: {chat.chat}")  # Access chat content
        #     print(f"User name: {chat.user.username}")  # Access user's username
        #     print(f"User email: {chat.user.email}")

        data = [{'chat': chat.chat, 'time': chat.created_at, 'username': chat.user.username} for chat in users_with_chats]

        return JsonResponse({'userChats': data})