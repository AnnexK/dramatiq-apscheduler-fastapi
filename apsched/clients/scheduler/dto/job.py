from datetime import datetime
from typing import Any
from pydantic import BaseModel
from .triggers import TriggerDto


class JobDto(BaseModel):
    id: str
    name: str
    func: str
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    trigger: TriggerDto
    next_run_time: datetime
