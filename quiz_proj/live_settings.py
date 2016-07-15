import os

from .base_settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carltaylor43$quiz_app_db',
        'USER': 'carltaylor43',
        'PASSWORD': '8sjhue4fgj98jhnd',
        'HOST': 'carltaylor43.mysql.pythonanywhere-services.com',
    }
}

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY')
