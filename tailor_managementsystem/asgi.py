"""
ASGI config for tailor_managementsystem tailor_managementsystem.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tailor_managementsystem.settings')

application = get_asgi_application()
