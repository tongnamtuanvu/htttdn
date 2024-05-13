"""
ASGI config for test_koalixcrm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
from django.conf import settings
settings.configure()
import os
from filebrowser.base import FileObject

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_koalixcrm.settings')

application = get_asgi_application()
