from enum import Enum


class TriggerType(str, Enum):
    CRON = "cron"
    INTERVAL = "interval"
