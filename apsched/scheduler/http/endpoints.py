from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from dependency_injector.wiring import inject, Provide

from apsched.scheduler.service import SchedulerService
from apsched.scheduler.service.errors import *

from .trigger_factory import TriggerFactory
from .models import AddJobRequest
from .models.job import map_job_to_job_model, Job
from .container import SchedulerContainer

router = APIRouter()


@router.get("/api/jobs")
@inject
async def get_all_jobs(
    scheduler: SchedulerService = Depends(Provide[SchedulerContainer.scheduler_service]),
) -> list[Job]:
    jobs = scheduler.get_jobs()
    return [map_job_to_job_model(job) for job in jobs]


@router.post("/api/jobs")
@inject
async def add_job(
    task: AddJobRequest,
    scheduler: SchedulerService = Depends(Provide[SchedulerContainer.scheduler_service]),
    trigger_factory: TriggerFactory = Depends(TriggerFactory),
):
    try:
        trigger = trigger_factory.make_trigger(task.trigger)
        scheduler.add_job(task.func, trigger, task.id_on_args, *task.args, **task.kwargs)
    except JobExists as exc:
        raise HTTPException(HTTPStatus.UNPROCESSABLE_ENTITY, str(exc))


@router.get("/api/jobs/{job_id}")
@inject
async def get_job_by_id(
    job_id: str, scheduler: SchedulerService = Depends(Provide[SchedulerContainer.scheduler_service])
):
    try:
        return map_job_to_job_model(scheduler.get_job(job_id))
    except JobNotFound as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(exc))


@router.delete("/api/jobs/{job_id}")
@inject
async def remove_task(
    job_id: str, scheduler: SchedulerService = Depends(Provide[SchedulerContainer.scheduler_service])
):
    try:
        scheduler.remove_job(job_id)
    except JobNotFound as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(exc))


@router.post("/api/jobs/{job_id}/force")
@inject
async def force_job(job_id: str, scheduler: SchedulerService = Depends(Provide[SchedulerContainer.scheduler_service])):
    try:
        scheduler.force_job(job_id)
    except JobNotFound as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(exc))
