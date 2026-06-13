from pydantic import BaseModel


class UserCreateBody(BaseModel):
    username: str
    email: str
    password: str

class UserCreateResponse(BaseModel):
    username: str
    email: str