from __future__ import absolute_import, unicode_literals

import os
import ssl

from celery import Celery
from celery.schedules import crontab
from pytz import timezone

moscow_tz = timezone('Europe/Moscow')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

redbeat_redis_url = os.environ.get('REDIS_URL', 'redis://redis:6379') + '/1'

schedule_time = crontab(hour=19, minute=0)


def get_celery_sll():
    return Celery(
        'backend',
        broker_use_ssl={
            'ssl_cert_reqs': ssl.CERT_NONE
        },
        redis_backend_use_ssl={
            'ssl_cert_reqs': ssl.CERT_NONE
        }
    )


def get_celery():
    return Celery('backend')


use_ssl = redbeat_redis_url.startswith('rediss://')
app = get_celery_sll() if use_ssl else get_celery()
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
