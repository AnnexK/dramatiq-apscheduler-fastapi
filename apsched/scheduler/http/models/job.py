from typing import Any
from datetime import datetime
from pydantic import BaseModel
from apscheduler.job import Job as SchedulerJob
from apscheduler.triggers.base import BaseTrigger
from apscheduler.triggers.cron import CronTrigger as SchedulerCronTrigger
from apscheduler.triggers.interval import IntervalTrigger as SchedulerIntervalTrigger
from .triggers import Trigger, CronTrigger, IntervalTrigger


class Job(BaseModel):
    id: str
    name: str
    func: str
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    trigger: Trigger
    next_run_time: datetime


def map_job_to_job_model(job: SchedulerJob) -> Job:
    def get_func_classifier(func: Any) -> str:
        return f"{func.__module__}:{func.__self__.__class__.__name__}.{func.__name__}"

    return Job(
        id=job.id,
        name=job.name,
        func=get_func_classifier(job.func),
        args=job.args,
        kwargs=job.kwargs,
        trigger=_map_trigger_to_trigger_model(job.trigger),
        next_run_time=job.next_run_time,
    )


def _map_trigger_to_trigger_model(trigger: BaseTrigger) -> Trigger:
    if isinstance(trigger, SchedulerCronTrigger):
        return _map_crontab_to_model(trigger)
    elif isinstance(trigger, SchedulerIntervalTrigger):
        return IntervalTrigger(
            weeks=trigger.weeks,
            days=trigger.days,
            hours=trigger.hours,
            minutes=trigger.minutes,
            seconds=trigger.seconds,
        )
    else:
        raise TypeError(f"Cannot map trigger with type {type(trigger)}")


def _map_crontab_to_model(cron_trigger: SchedulerCronTrigger) -> CronTrigger:
    def extract_crontab_value(key: str) -> str:
        field = next(filter(lambda fld: fld.name == key, cron_trigger.fields))
        return str(field)

    return CronTrigger(
        minute=extract_crontab_value("minute"),
        hour=extract_crontab_value("hour"),
        day_of_month=extract_crontab_value("day"),
        month=extract_crontab_value("month"),
        day_of_week=extract_crontab_value("day_of_week"),
    )
