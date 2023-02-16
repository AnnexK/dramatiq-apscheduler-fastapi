from typing import Literal
from .base_trigger import BaseTrigger
from .trigger_type import TriggerType


class CronTrigger(BaseTrigger):
    type: Literal[TriggerType.CRON] = TriggerType.CRON
    minute: str
    hour: str
    day_of_month: str
    month: str
    day_of_week: str
