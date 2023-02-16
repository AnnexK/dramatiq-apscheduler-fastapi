from http import HTTPStatus

import requests
import pydantic

from .dto import JobDto, ResponseError, AddJobRequestDto
from .errors import *


class ScheduleServiceClient:
    """
    Клиент к веб-сервису планировщика задач.
    """

    def __init__(self, service_url: str):
        self._url = service_url

    def get_all_jobs(self) -> list[JobDto]:
        endpoint = f"{self._url}/api/jobs"

        with requests.get(endpoint) as response:
            if not response.ok:
                raise UnexpectedResponseError(response)
            return pydantic.parse_raw_as(list[JobDto], response.content)

    def get_job(self, job_id: str) -> JobDto:
        endpoint = f"{self._url}/api/jobs/{job_id}"
        with requests.get(endpoint) as response:
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise JobNotFound(job_id)
            if not response.ok:
                raise UnexpectedResponseError(response)
            return JobDto.parse_raw(response.content)

    def add_job(self, request: AddJobRequestDto):
        endpoint = f"{self._url}/api/jobs"
        with requests.post(endpoint, data=request.dict()) as response:
            if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                error = ResponseError.parse_raw(response.content)
                raise CannotProcessRequest("add_job", error.detail)
            if not response.ok:
                raise UnexpectedResponseError(response)
