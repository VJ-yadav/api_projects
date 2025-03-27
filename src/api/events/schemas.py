from pydantic import BaseModel
from typing import List



class EventCreateSchema(BaseModel):
    path: str


class EventSchema(BaseModel):
    id: int


class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: int
