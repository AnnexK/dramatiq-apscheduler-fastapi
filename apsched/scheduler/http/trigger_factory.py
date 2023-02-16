from apscheduler.triggers.base import BaseTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from .models.triggers import Trigger, CronTrigger as CronTriggerModel, IntervalTrigger as IntervalTriggerModel
from .models.triggers.trigger_type import TriggerType


class TriggerFactory:
    def make_trigger(self, trigger_data: Trigger) -> BaseTrigger:
        match trigger_data.type:
            case TriggerType.CRON:
                return self._make_cron_trigger(trigger_data)
            case TriggerType.INTERVAL:
                return self._make_interval_trigger(trigger_data)
            case _:
                raise Exception("unknown trigger type")

    def _make_cron_trigger(self, cron_trigger_data: CronTriggerModel) -> CronTrigger:
        return CronTrigger(
            minute=cron_trigger_data.minute,
            hour=cron_trigger_data.hour,
            day=cron_trigger_data.day_of_month,
            month=cron_trigger_data.month,
            day_of_week=cron_trigger_data.day_of_week,
        )

    def _make_interval_trigger(self, interval_trigger_data: IntervalTriggerModel) -> IntervalTrigger:
        return IntervalTrigger(
            weeks=interval_trigger_data.weeks,
            days=interval_trigger_data.days,
            hours=interval_trigger_data.hours,
            minutes=interval_trigger_data.minutes,
            seconds=interval_trigger_data.seconds,
        )
