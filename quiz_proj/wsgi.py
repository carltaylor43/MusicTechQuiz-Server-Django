"""
WSGI config for quiz_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_proj.live_settings")
os.environ['SECRET_KEY'] = 'not_real_key_dont_worry'

application = get_wsgi_application()
