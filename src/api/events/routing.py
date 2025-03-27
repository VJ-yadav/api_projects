import os
from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema, EventCreateSchema


router = APIRouter()


@router.get("/")
def get_events_list() -> EventListSchema:
    print(os.environ.get("SECRET_KEY"),"SeK")
    print(os.environ.get("DATABASE_URL"))
    return {"results": [{"id": 1}, {"id": 2}, {"id": 3}], "count": 3}


@router.get("/{events_id}")
def get_event(events_id: int) -> EventSchema:
    return {"id": events_id}



@router.post("/")
def create_events(payload: EventCreateSchema) -> EventSchema:
    return {
        print(payload)
        
    }