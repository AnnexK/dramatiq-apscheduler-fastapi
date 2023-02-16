from fastapi import FastAPI

from .container import SchedulerContainer
from . import endpoints


def create_app() -> FastAPI:
    container = SchedulerContainer()
    container.init_resources()
    container.wire(modules=[".endpoints"])
    container.scheduler_service()

    app = FastAPI()
    app.include_router(endpoints.router)

    return app


app = create_app()
