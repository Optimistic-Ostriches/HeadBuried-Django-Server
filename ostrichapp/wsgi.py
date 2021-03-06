"""
WSGI config for ostrichapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Use production settings on Azure
if os.environ.get('DJANGO_ENV') == 'production':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ostrichapp.production')
# Use local debug settings on development
else:
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ostrichapp.settings')

application = get_wsgi_application()
