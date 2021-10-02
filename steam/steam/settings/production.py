from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your.doma.by']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'steam',
        'USER': 'steamadmin',
        'PASSWORD': '2554963demidovT',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


STATIC_URL = '/static/'
STATIC_ROOT # = path/to/file

MEDIA_ROOT # = path/to/file
MEDIA_URL = '/media/'