from datetime import datetime
from pydantic import BaseModel


class Tagin(BaseModel):
    tag: str

class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str

class Tagout(BaseModel):
    tag: str
    created: datetime
    