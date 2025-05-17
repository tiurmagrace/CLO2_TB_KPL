# services/export_service.py
import json
from datetime import date
from models.event import Event
from typing import List

def export_events(events: List[Event]) -> str:
    def event_serializer(obj):
        if isinstance(obj, date):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")
    
    return json.dumps([event.model_dump() for event in events], 
                     indent=4, ensure_ascii=False, default=event_serializer)