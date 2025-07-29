from pydantic import BaseModel


class HelloResponse(BaseModel):
    message: str = "Hello, World!"


class ErrorResponse(BaseModel):
    error: str
    message: str
