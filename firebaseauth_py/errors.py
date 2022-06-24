from typing import List, TypedDict


class ErrorItem(TypedDict):
    domain: str
    reason: str
    mesage: str


class ErrorPayload(TypedDict):
    errors: List[ErrorItem]
    code: int
    message: str


class ErrorResponse(TypedDict):
    error: ErrorPayload
