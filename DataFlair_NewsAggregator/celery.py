from __future__ import absolute_import, unicode_literals
from .settings import BROKER_URL, BACKEND_URL
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DataFlair_NewsAggregator.settings')

app = Celery('news', broker=BROKER_URL, backend=BACKEND_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
