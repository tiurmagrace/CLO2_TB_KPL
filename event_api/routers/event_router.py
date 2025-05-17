# routers/event_router.py
from fastapi import APIRouter, HTTPException, status, Query
from models.event import Event
from models.participant import Participant
from models.rsvp_status import RSVPStatus
from models.confirmation import Confirmation
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

@router.post("/{event_id}/participants", status_code=status.HTTP_201_CREATED)
def add_participant(event_id: int, participant: Participant):
    if event_id < 0 or event_id >= len(events):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    events[event_id].participants.append(participant)
    return {"message": f"{participant.name} ditambahkan ke event {event_id}"}

@router.put("/{event_id}/rsvp")
def update_rsvp(event_id: int, name: str = Query(...), confirmation: str = Query(...)):
    if event_id < 0 or event_id >= len(events):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

    # Validasi konfirmasi
    confirmation = confirmation.lower()
    if confirmation not in [c.value for c in Confirmation]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Nilai konfirmasi harus berupa '{Confirmation.YA}' atau '{Confirmation.TIDAK}'"
        )

    for p in events[event_id].participants:
        if p.name.lower() == name.lower():
            # Pastikan logika yang benar: 'ya' -> ATTENDING, 'tidak' -> NOT_ATTENDING
            if confirmation == Confirmation.YA.value:
                p.status = RSVPStatus.ATTENDING
            elif confirmation == Confirmation.TIDAK.value:
                p.status = RSVPStatus.NOT_ATTENDING
            return {"message": f"RSVP {p.name} diperbarui menjadi {p.status.value}"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participant not found")