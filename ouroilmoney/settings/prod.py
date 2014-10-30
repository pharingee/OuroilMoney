
# settings/dev.py

from base import *
import os

DEBUG = False

TEMPLATE_DEBUG = DEBUG

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

INSTALLED_APPS += ('storages')

MIDDLEWARE_CLASSES += ()

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*.herokuapp.com').split(',')

CORS_ORIGIN_ALLOW_ALL = True

SWAGGER_SETTINGS = {
    "exclude_namespaces": [],
    "api_version": '1.0',  # Specify your API's version
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',

    ],
    "api_key": '',  # An API key
    "is_authenticated": True,  # Set to True to enforce user authentication,
    "is_superuser": True,  # Set to True to enforce admin only access
}
