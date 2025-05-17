# routers/export_router.py
from fastapi import APIRouter, Response
from services.export_service import export_events
from routers.event_router import events

router = APIRouter()

@router.get("/events")
def export_event_data():
    json_data = export_events(events)
    return Response(content=json_data, media_type="application/json")