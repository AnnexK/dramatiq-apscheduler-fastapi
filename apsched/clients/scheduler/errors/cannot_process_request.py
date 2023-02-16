from .base import SchedulerServiceError


class CannotProcessRequest(SchedulerServiceError):
    def __init__(self, request_type: str, reason: str):
        self.request_type = request_type
        self.reason = reason

    def __str__(self) -> str:
        return f"Cannot process request of type {self.request_type}. Reason: {self.reason}."
