# settings/dev.py

from base import *


DEBUG = True

TEMPLATE_DEBUG = DEBUG

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR('staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR('media')

INSTALLED_APPS += ()

MIDDLEWARE_CLASSES += ()
