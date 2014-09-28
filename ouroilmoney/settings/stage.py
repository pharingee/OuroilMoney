from base import *


DEBUG = False

TEMPLATE_DEBUG = DEBUG

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

INSTALLED_APPS += ()

MIDDLEWARE_CLASSES += ()
ALLOWED_HOSTS=os.environ.get('ALLOWED_HOSTS', '.herokuapp.com').split(':')

