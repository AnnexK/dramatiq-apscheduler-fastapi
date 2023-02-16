from pydantic import BaseModel


class ResponseError(BaseModel):
    detail: str
