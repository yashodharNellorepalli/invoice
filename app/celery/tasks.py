from celery import Celery
from app.utils.helpers import get_config_value


CELERY_BROKER = get_config_value("CELERY_BROKER")
CELERY_BACKEND = get_config_value("CELERY_BACKEND")

app = Celery('task', backend=CELERY_BACKEND, broker=CELERY_BROKER)


@app.task()
def task():
    pass
