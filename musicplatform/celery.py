import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

app = Celery('musicplatform')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY_CONF')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'hommos': {
        'task': 'musicplatform.tasks.hommos',
        'schedule': 5,
    },
    }

@app.task(bind=True)
def debug_task(self):
     print(f'Request: {self.request!r}')