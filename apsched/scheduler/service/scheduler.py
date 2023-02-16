import hashlib
import json
import logging

from typing import Any
from datetime import datetime

from apscheduler.jobstores.base import JobLookupError, ConflictingIdError
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.job import Job
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.base import BaseTrigger

from apsched.config.app_config import settings

from .errors import *

logging.basicConfig()
logging.getLogger("apscheduler").setLevel(logging.DEBUG)


class SchedulerService:
    def __init__(self):
        self._jobstore = SQLAlchemyJobStore(url=settings.SCHEDULER.JOBSTORE.SQL.URL)
        self._scheduler = BackgroundScheduler()
        self._scheduler.add_jobstore(self._jobstore)
        self._scheduler.start()

    def add_job(self, func: str, trigger: BaseTrigger, id_by_args: bool, *args, **kwargs):
        try:
            task_id = self._generate_task_id_by_args(func, args, kwargs) if id_by_args else None
            self._scheduler.add_job(func, trigger, args, kwargs, id=task_id, misfire_grace_time=None)
        except ConflictingIdError:
            raise JobExists(task_id)

    def get_jobs(self) -> list[Job]:
        return self._scheduler.get_jobs()

    def get_job(self, job_id: str) -> Job:
        try:
            return self._scheduler.get_job(job_id)
        except JobLookupError:
            raise JobNotFound(job_id)

    def _generate_task_id_by_args(self, func: str, args: tuple[Any, ...], kwargs: dict[str, Any]) -> str:
        args_hash = hashlib.md5(json.dumps({"args": args, "kwargs": kwargs}).encode()).hexdigest()
        return f"{func}-{args_hash}"

    def remove_job(self, job_id: str):
        try:
            self._scheduler.remove_job(job_id)
        except JobLookupError:
            raise JobNotFound(job_id)

    def force_job(self, job_id: str):
        try:
            self._scheduler.modify_job(job_id, next_run_time=datetime.now())
        except JobLookupError:
            raise JobNotFound(job_id)
