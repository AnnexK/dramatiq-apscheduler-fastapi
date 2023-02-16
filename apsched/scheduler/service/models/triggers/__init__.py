from typing import Annotated
from pydantic import Field
from .cron_trigger import CronTrigger
from .interval_trigger import IntervalTrigger


Trigger = Annotated[CronTrigger | IntervalTrigger, Field(discriminator="type")]
