from apsched.config.app_config import settings
from apsched.tasks import BaseTask
from apsched.tasks.retry_mixin import RetryMixin


class InstantTask(BaseTask):
    class Meta:
        abstract = True

    def run(self, *args, **kwargs):
        self.send(*args, **kwargs)
