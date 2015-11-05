
# settings/dev.py

from base import *
import os

DEBUG = False

TEMPLATE_DEBUG = DEBUG

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

INSTALLED_APPS += ('storages',)

MIDDLEWARE_CLASSES += ()

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

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

STATICFILES_STORAGE = 'ouroilmoney.utils.s3.StaticRootS3BotoStorage'

DEFAULT_FILE_STORAGE = 'ouroilmoney.utils.s3.MediaRootS3BotoStorage'

THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_QUERYSTRING_AUTH = False

STATIC_DIRECTORY = '/static/'

MEDIA_DIRECTORY = '/media/'

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY
