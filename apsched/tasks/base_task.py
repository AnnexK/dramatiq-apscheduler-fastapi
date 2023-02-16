from dramatiq import GenericActor
from apsched.config.app_config import settings
from .retry_mixin import RetryMixin
from .task_meta import BaseTaskMeta


class BaseTask(GenericActor, metaclass=BaseTaskMeta):
    class Meta(RetryMixin):
        abstract = True
        queue_name = settings.SCHEDULER.BROKER.QUEUE_NAME
