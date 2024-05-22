"""
URL configuration for ai_chat_assistant_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ai.views import ask, askImage, signup, signinGuest, signinUser, getAllUsers
from chat.views import addChat, getChats, addGroupChat, getGroupChats, addPrivateChat, getPrivateChats

urlpatterns = [
    path('ask/', ask, name='ask'),
    path('askImage/', askImage, name='askImage'),
    path('signup/', signup, name='signup'),
    path('signin/guest/', signinGuest, name='signin/guest'),
    path('signin/user/', signinUser, name='signin/user'),
    path('getAllUsers/', getAllUsers, name='getAllUsers'),

    path('addChat/', addChat, name='addChat'),
    path('getChats/', getChats, name='getChats'),
    path('addGroupChat/', addGroupChat, name='addGroupChat'),
    path('getGroupChats/<int:userId>/', getGroupChats, name='getGroupChats'),
    path('addPrivateChat/', addPrivateChat, name='addPrivateChat'),
    path('getPrivateChats/<int:userId>/', getPrivateChats, name='getPrivateChats'),

    
    path('admin/', admin.site.urls),

]
