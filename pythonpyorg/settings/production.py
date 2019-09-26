from .base import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY_PROD")

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME_PROD"),
        'USER': os.environ.get("DB_USER_PROD"),
        'PASSWORD': os.environ.get("DB_PASSW_PROD"),
        'HOST': os.environ.get("DB_HOST_PROD"),
        'PORT':  os.environ.get("DB_PORT_PROD"),
    }
}