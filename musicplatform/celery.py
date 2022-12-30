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
#        S  * M  * H  * D
period = 60 * 60 * 24 * 14
app.conf.beat_schedule = {
    'hommos': {
        'task': 'albums.tasks.fetch_data',
        'schedule': period,
    },
    }

@app.task(bind=True)
def debug_task(self):
     print(f'Request: {self.request!r}')