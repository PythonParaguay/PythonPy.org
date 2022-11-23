import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY_DEV")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS=['*']
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME_DEV"),
        'USER': os.environ.get("DB_USER_DEV"),
        'PASSWORD': os.environ.get("DB_PASSW_DEV"),
        'HOST': os.environ.get("DB_HOST_DEV"),
        'PORT':  os.environ.get("DB_PORT_DEV"),
    }
}

try:
    from .local import *
except ImportError:
    pass
