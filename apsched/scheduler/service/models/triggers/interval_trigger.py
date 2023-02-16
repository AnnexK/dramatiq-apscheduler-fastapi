from typing import Literal
from enum import Enum
from .base_trigger import BaseTrigger
from .trigger_type import TriggerType


class IntervalTrigger(BaseTrigger):
    type: Literal[TriggerType.INTERVAL] = TriggerType.INTERVAL
    weeks: int = 0
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
