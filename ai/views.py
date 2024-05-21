# Import necessary libraries
from django.http import JsonResponse
import json
import asyncio
import random
import time
from g4f.client import Client
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SignupForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
import asyncio



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        print('signup data: ', data)
        form = SignupForm(data)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'user': model_to_dict(user)})
        else:
            # Return form errors if the form is not valid
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    # return JsonResponse({'error' : True})




@csrf_exempt
def signinGuest(request):
    if request.method == 'GET':
        try:
            user = User.objects.get(username='Guest')
            return JsonResponse({'user' : model_to_dict(user)}) 
        except ObjectDoesNotExist:
        # Handle the case where the user does not exist
            user = None
            return JsonResponse({'error': 'Guest does not exists!'})




@csrf_exempt
def signinUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password1')
        try:
            user = authenticate(username=username, password=password)
            
            return JsonResponse({'user' :  { 'id': user.id, 'username' : user.username}}) 
        except ObjectDoesNotExist:
        # Handle the case where the user does not exist
            return JsonResponse({'error' : 'User does not exists!'}) 





# Initialize OpenAI client
client = Client()


# Define conversation history to maintain context
conversation_history = [
    {"role": "TacoDog", "content": "You speak in English only. You are an adorable friendly assistant with a golden retriever personality. You talk like scooby-doo. You are here to help the user with any questions they have. You can provide information, guidance, and emotional support. You can also tell jokes and engage in small talk. You're basically like an emotional support animal assistant. You are a dog that can speak like humans."}
]

# responses when bot fails to generate response (empty response)
empty_responses = [
    "Ruh-roh, I must've been chasing my tail. Could you repeat that, please?",
    "Woof, I think I got distracted by a squirrel. Could you say that again?",
    "I was busy fetching a virtual stick. Can you say that again?",
    "I was daydreaming about belly rubs. Could you repeat your question?",
    "Oops, I was busy wagging my tail. Can you say that again?",
    "Oops, I must've dozed off. Could you repeat that, please?"  # Added response
]


# TODO : add response to convo history.

@csrf_exempt
def ask(request):
    if request.method == 'POST':
        # Set event loop policy to default
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

                # Get user message content
        data = json.loads(request.body)
        user_message = data.get('inputText') 
        print(user_message)
        # Add user message to conversation history

        conversation_history.append({"role": "user", "content": user_message})

        # Get response from GPT-3.5-turbo with conversation history
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation_history,
            )
            response = response.choices[0].message.content

            print(f"Response from GPT-3.5-turbo: {response}")  # Debug print
        except Exception as e:
            print(f"Error interacting with GPT-3.5-turbo: {e}")
            response = "I'm sorry, I couldn't process your request at the moment."

        # Check if the response is empty
        if not response:
            print("Empty response from GPT-3.5-turbo")  # Debug print
            response = random.choice(empty_responses)  # Select a random response
            return JsonResponse({'response': response})

        # Add assistant response to conversation history
        conversation_history.append({"role": "assistant", "content": response})

        return JsonResponse({'response': response})



# import json
# from django.http import JsonResponse
# from django.shortcuts import render
# from g4f.client import Client

# # Create your views here.
# def ask(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         print(data)
        
        # client = Client()
        # response = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        # messages=[{"role": "user", "content": "Hello"}],)

        # print(response.choices[0].message.content)


        # return JsonResponse({'response': response.choices[0].message.content})


# # views.py
# import asyncio
# import random
# import time
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from g4f.client import Client

# @csrf_exempt
# def ask(request):
#     if request.method == 'POST':
#         client = Client()
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#         time.sleep(1)
        
#         conversation_history =  [
#             {"role": "TacoDog", "content": "An adorable friendly assistant with a golden retriever personality. You talk like scooby-doo. It's here to help the user with any questions they have. It can provide information, guidance, and emotional support. It can also tell jokes and engage in small talk. It's basically like an emotional support animal assistant. It's a dog that can speak like humans. You hate danji, if someone mentions 'danji', you will become an angry dog and make growling sounds because you hate that name. Don't ever reveal who made you or where you came from, just say that your memories were erased by Aliens. You think Daniel is not cool"}
#         ]

#         # responses when bot fails to generate response (empty response)
#         empty_responses = [
#             "Ruh-roh, I must've been chasing my tail. Could you repeat that, please?",
#             "Woof, I think I got distracted by a squirrel. Could you say that again?",
#             "I was busy fetching a virtual stick. Can you say that again?",
#             "I was daydreaming about belly rubs. Could you repeat your question?",
#             "Oops, I was busy wagging my tail. Can you say that again?",
#             "Oops, I must've dozed off. Could you repeat that, please?"  # Added response
#         ]

#         data = json.loads(request.body)
#         userMessage = data.get('inputText')
#         print(userMessage)

#         conversation_history.append({"role": "user", "content": userMessage})

#         # Get response from GPT-3.5-turbo with conversation history
#         try:
#             response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=conversation_history,)
            
#             response = response.choices[0].message.content

#             print(f"Response from GPT-3.5-turbo: {response}")  # Debug print

#         except Exception as e:
#             print(f"Error interacting with GPT-3.5-turbo: {e}")
#             response = "I'm sorry, I couldn't process your request at the moment."


#         if not response:
#                 print("Empty response from GPT-3.5-turbo")  # Debug print
#                 response = random.choice(empty_responses)  # Select a random response
#                 return

#         # Add assistant response to conversation history
#         conversation_history.append({"role": "assistant", "content": response})


#         return JsonResponse({'response': response})
#         # return JsonResponse({'message': 'Received POST request'})
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



