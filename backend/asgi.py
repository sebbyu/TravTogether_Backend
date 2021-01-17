"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# import os
# from backend.current_settings import CURRENT_SETTING

# from django.core.asgi import get_asgi_application

# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', CURRENT_SETTING)

# application = get_asgi_application()


import os
from channels.routing import get_default_application
import django
from backend.current_settings import CURRENT_SETTING

os.environ.setdefault("DJANGO_SETTINGS_MODULE", CURRENT_SETTING)
django.setup()
application = get_default_application()