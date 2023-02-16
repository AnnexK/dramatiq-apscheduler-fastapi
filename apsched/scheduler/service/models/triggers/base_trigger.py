from pydantic import BaseModel, Field
from .trigger_type import TriggerType


class BaseTrigger(BaseModel):
    type: TriggerType
