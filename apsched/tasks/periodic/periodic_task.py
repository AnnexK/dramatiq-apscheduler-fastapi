from apscheduler.triggers.base import BaseTrigger
from apsched.tasks.base_task import BaseTask


class PeriodicTask(BaseTask):
    class Meta:
        abstract = True

    def _trigger(self) -> BaseTrigger:
        """
        Получить объект, управляющий периодичностью запуска задачи
        (например, расписание Cron).
        """
        raise NotImplementedError

    def name(self) -> str:
        """
        Вернуть имя задачи.
        По умолчанию это классификатор задачи.
        Можно переопределить в подклассах.
        """
        return self._task_func()

    # TODO: добавить генератор ID

    def _task_func(self) -> str:
        """
        Получить классификатор задачи для APScheduler.
        """
        return f"{self.__module__}:{self.__class__.__name__}.send"

    def run(self, *args, **kwargs):
        pass
