"""
WSGI config for ouroilmoney project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ouroilmoney.settings")

from django.core.wsgi import get_wsgi_application
# Cling not used because we dont want to serve staticfiles in production
application = get_wsgi_application()
