from dependency_injector import containers, providers

from apsched.scheduler.service import SchedulerService


class SchedulerContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])
    scheduler_service = providers.Singleton(SchedulerService)
