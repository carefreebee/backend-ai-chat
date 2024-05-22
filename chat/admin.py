from django.contrib import admin

from .models import Chat, GroupChat, PrivateChat
# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    list_display = ( 'user','chat', 'created_at')

class GroupChatAdmin(admin.ModelAdmin):
    list_display = ( 'name','created_by', 'is_deleted')


    
admin.site.register(Chat, ChatAdmin)
admin.site.register(GroupChat, GroupChatAdmin)
admin.site.register(PrivateChat)