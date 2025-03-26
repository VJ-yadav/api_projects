from fastapi import APIRouter
from .schemas import EventSchema

router = APIRouter()


@router.get("/")
def get_events():
    return {"items": [1, 2, 3]}


@router.get("/{events_id}")
def get_event(events_id: int) -> EventSchema:
    return {"id": events_id}
