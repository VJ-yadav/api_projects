# from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import List, Optional


class EventSchema(SQLModel):
    id: int
    page:Optional[str] = Field(default=None)
    description:Optional[str] = ""

class EventCreateSchema(SQLModel):
    path: str
    description:Optional[str] = ""


class EventListSchema(SQLModel):
    results: List[EventSchema]
    count: int
