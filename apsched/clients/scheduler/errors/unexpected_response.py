from requests import Response
from .base import SchedulerServiceError


class UnexpectedResponseError(SchedulerServiceError):
    def __init__(self, response: Response):
        self._response_status = response.status_code
        self._response_content = response.content

    def __str__(self) -> str:
        return (
            "Unexpected response from server."
            f"Status code: {self._response_status}."
            f"Content: {self._response_content!r}."
        )
