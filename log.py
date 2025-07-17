from typing import Any
from cloudio.task import PythonCloudioTask



class LogMessageTask(PythonCloudioTask):
    requirements = "airflow_team_2/requirements.txt"

    def run(message: str = "Hello, World!"):
        from loguru import logger
        logger.info(message)
        raise

    @staticmethod
    def rollback(run_output: Any, message: str = "Hello, World!"):
        from loguru import logger
        logger.info(run_output)
        logger.info(message)



# @task.virtualenv(
#     task_id="log_message_rollback",
#     requirements="airflow_team_2/requirements.txt",
#     system_site_packages=False,
# )
# def log_message_rollback(rollback_tasks: list[str] = []):
#     if "log_message" in rollback_tasks:
#         from loguru import logger
#         logger.info("dd")
#     else:
#         print("No rollback needed for log_message")


# @task.virtualenv(
#     task_id="log_message", requirements="airflow_team_2/requirements.txt", system_site_packages=False
# )
# def log_message(message):
#     from loguru import logger
#     logger.info(message)
