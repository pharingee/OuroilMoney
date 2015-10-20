# settings/dev.py

from base import *


DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR('staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR('media')

INSTALLED_APPS += ()

MIDDLEWARE_CLASSES += ()
