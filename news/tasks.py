from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import shared_task

from .views import scrape

logger = get_task_logger(__name__)


@task(name="scrape")
def data():
    logger.info("News Refreshed!!!")
    scrape()
    return True
