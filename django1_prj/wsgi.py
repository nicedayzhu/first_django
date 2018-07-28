"""
WSGI config for django1_prj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django1_prj.settings")

application = Cling(get_wsgi_application())
