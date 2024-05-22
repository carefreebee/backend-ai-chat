import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .models import Chat, GroupChat, PrivateChat
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from django.core import serializers
from django.db.models import Q

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
            return JsonResponse({'success': True, 'chatId': chat.id})
        
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

        data = [{'chat': chat.chat, 'time': chat.created_at, 'user': model_to_dict(chat.user)} for chat in users_with_chats]

        return JsonResponse({'userChats': data})
    

@csrf_exempt
def addGroupChat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        group_name =data.get('name')
        creator_id = data.get('creator_id')
        userIds = data.get('userIds')

        group_chat = GroupChat.objects.create(name=group_name, created_by=creator_id)
        for userId in userIds:
            try:
                user = User.objects.get(id=userId)
                group_chat.users.add(user)
                
            except User.DoesNotExist:
                print(f"User with username {userId} does not exist.")
                return JsonResponse({'error': f'UserId {userId} does not exist!'})
        
        group_chat.save()
        return JsonResponse({'sucess': f'Groupchat {group_name} created successfully'})
            



@csrf_exempt
def getGroupChats(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        userId = data.get('userId')
        try: 
            user_group_chats = User.objects.get(id=userId).groupchat_set.all();
            return JsonResponse({'userGroupChats' : model_to_dict(user_group_chats)})
        except ObjectDoesNotExist:
            return JsonResponse({'erorr' : "GroupChats with user dont exist!"})


@csrf_exempt
def deleteGroupChat(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        groupId = data.get('groupId')
        
        group_chat = GroupChat.objects.get(id = groupId)
        group_chat.is_deleted = True
        group_chat.save()
        
        return JsonResponse({'success' : 'Groupchat deleted!'})
    


@csrf_exempt
def addPrivateChat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        userIds = data.get('userIds')
        chatIds = data.get('chatIds')
        print(userIds, chatIds, data)
        try: 
            private_chat = PrivateChat.objects.filter(user1_id__in=userIds).filter(user2_id__in=userIds).first()
            # print(private_chat)
            if private_chat:
                chats = Chat.objects.filter(id__in=chatIds)
                private_chat.chats.add(*chats)
                # for chatId in chatIds:
                #     chat = Chat.objects.get(id=chatId)
                #     private_chat.chats.add(chat)
                # print('private char', private_chat)
            
            else:
                # Create a new private chat
                users = User.objects.filter(id__in=userIds)
                chats = Chat.objects.filter(id__in=chatIds)
                # print('users chat, ', users, chats)
                private_chat = PrivateChat.objects.create(user1=users[0], user2=users[1])
                private_chat.chats.add(*chats)
                # print('new', private_chat)

            
            # print('print', private_chat, model_to_dict(private_chat))

            chats = [{'chat': chat.chat, 'time': chat.created_at, 'user': model_to_dict(chat.user)} for chat in model_to_dict(private_chat).get('chats')]
            # print(chats)

            def extract(user):
                user = model_to_dict(user)
                return {'id': user.get('id'), 'username' : user.get('username')}

            private_chat = {'id': private_chat.id, 'user1': extract(private_chat.user1), 'user2':extract(private_chat.user2), 'chats': chats}
            # print(private_chat)
            return JsonResponse({'success': 'PrivateChat created successfully', 'privatechat' : private_chat})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


        


@csrf_exempt
def getPrivateChats(request, userId):
    if request.method == 'GET':
        
        current_user_id = userId
        try:
            private_chats = PrivateChat.objects.select_related('user1', 'user2').filter(Q(user1=current_user_id) | Q(user2=current_user_id))            
            # print(private_chats)

            new_private_chats = []
            for private_chat in private_chats:
                chats = [{'chat': chat.chat, 'time': chat.created_at, 'user': model_to_dict(chat.user)} for chat in model_to_dict(private_chat).get('chats')]
                # print(chats)

                def extract(user):
                    user = model_to_dict(user)
                    return {'id': user.get('id'), 'username' : user.get('username')}

                private_chat = {'id': private_chat.id, 'user1': extract(private_chat.user1), 'user2':extract(private_chat.user2), 'chats': chats}
                # print(private_chat)
                new_private_chats.append(private_chat)

            # print('new',new_private_chats)

            return JsonResponse({'success' : True, 'private_chats' : new_private_chats})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})



@csrf_exempt
def deletePrivateChat(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        groupId = data.get('groupId')
        
        group_chat = GroupChat.objects.get(id = groupId)
        group_chat.is_deleted = True
        group_chat.save()
        
        return JsonResponse({'success' : 'Groupchat deleted!'})



        