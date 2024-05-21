"""
WSGI config for ai_chat_assistant_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import asyncio
import platform

# Set event loop policy based on platform
if platform.system() != 'Windows':
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_chat_assistant_backend.settings')

application = get_wsgi_application()
