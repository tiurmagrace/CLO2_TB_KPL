# routers/event_router.py 
from fastapi import APIRouter, HTTPException, status
from models.event import Event
from typing import List

router = APIRouter()

events: List[Event] = []

@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(event: Event):
    events.append(event)
    return event

@router.get("/", response_model=List[Event])
def list_events():
    return events