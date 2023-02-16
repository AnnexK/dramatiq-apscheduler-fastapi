class JobNotFound(Exception):
    def __init__(self, job_id: str):
        self.job_id = job_id

    def __str__(self) -> str:
        return f"Job with id {self.job_id} not found."
