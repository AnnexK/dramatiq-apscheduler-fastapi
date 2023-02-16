from typing import Annotated
from pydantic import Field
from .cron_trigger import CronTriggerDto
from .interval_trigger import IntervalTriggerDto


TriggerDto = Annotated[CronTriggerDto | IntervalTriggerDto, Field(discriminator="type")]

__all__ = ["TriggerDto", "CronTriggerDto", "IntervalTriggerDto"]
