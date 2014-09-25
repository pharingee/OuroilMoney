# settings/dev.py

from base import *


DEBUG = True

TEMPLATE_DEBUG = DEBUG

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

CORS_ORIGIN_REGEX_WHITELIST = ('localhost', "local.host")

INSTALLED_APPS += ()

MIDDLEWARE_CLASSES += ()
