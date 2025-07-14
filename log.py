from airflow.sdk import task
from loguru import logger


@task
def log_message():
    logger.info("blablabla")
