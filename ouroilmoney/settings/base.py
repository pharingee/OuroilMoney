"""
Django settings for ouroilmoney project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


PROJECT_DIR =  os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BASE_DIR = lambda * x : os.path.join(PROJECT_DIR, *x)



ADMINS  = (
    ('obeng william', 'obeng.kojo.william@gmail.com')
)

SECRET_KEY = os.environ.get('SECRET_KEY')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!


#  todo: verify allowed_host based on enviroments
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


THIRD_PARTY_APPS =  (
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders'
    )

LOCAL_APPS =(
    'ouroilmoney.utils',
    'ouroilmoney.apps.reports',
    'ouroilmoney.apps.revenues',
    'ouroilmoney.apps.allocations',
    'ouroilmoney.apps.liftings',
    'ouroilmoney.apps.projects',
    )

INSTALLED_APPS =  THIRD_PARTY_APPS + INSTALLED_APPS  + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ouroilmoney.urls'

WSGI_APPLICATION = 'ouroilmoney.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config()
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Accra'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# provide specific url from /api/v1.o/
CORS_URL_REGEX = r'^/api/.*$'



SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Ouroilmoney',
    'MENU':  (
        'sites',
        {'label': 'Settings', 'icon':'icon-cog', 'models': (
            'auth.group' ,
            {'model': 'auth.user', 'label': 'Staff'}
        )},

        {'app':'reports', 'label': 'Reports', 'icon': 'icon-file'},
        {'app':'revenues', 'label': 'Revenues', 'icon': 'icon-tint'},
        {'app':'liftings', 'label': 'Liftings', 'icon': 'icon-leaf'},
        {'app':'allocations', 'label': 'Allocations', 'icon': 'icon-calendar' , 'models':(
            'allocations.annualbudgetallocation',
            'allocations.confirmallocation')},

        {'app':'projects', 'label': 'Projects', 'icon': 'icon-calendar', 'models':(
            'projects.annualbudgetsector', 'projects.annualbudgetproject',
            'projects.confirmsector','projects.confirmproject'
            '')},
        )

}


TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)



SWAGGER_SETTINGS = {
    "exclude_namespaces": [],
    "api_version": '1.0',  # Specify your API's version

    "is_authenticated": False,  # Set to True to enforce user authentication,
    "is_superuser": False,  # Set to True to enforce admin only access
}


