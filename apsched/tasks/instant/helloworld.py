from .instant_task import InstantTask
from apsched.tasks.retry_mixin import RetryMixin


class HelloWorld(InstantTask):
    def perform(self):
        print("Hello world!")
