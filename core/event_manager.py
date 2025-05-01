from typing import List
from models.event import Event
from models.participant import Participant
from lib.utils import save_to_file

events: List[Event] = []

# Tambah Event
def tambah_event(title: str, location: str, date: str) -> Event:
    new_event = Event(title, location, date)
    events.append(new_event)
    return new_event

# Tambah Peserta ke Event
def tambah_peserta(event_idx: int, participant_name: str):
    participant = Participant(participant_name)
    events[event_idx].participants.append(participant)

# Atur RSVP
def atur_rsvp(event_idx: int, participant_name: str, confirmation: str) -> bool:
    event = events[event_idx]
    for participant in event.participants:
        if participant.name.lower() == participant_name.lower():
            if confirmation.lower() == "ya":
                participant.status = participant.status.CONFIRMED
            else:
                participant.status = participant.status.DECLINED
            return True
    return False

# Export data Event ke file
def export_data() -> str:
    data = []
    for e in events:
        event_info = {
            "title": e.title,
            "location": e.location,
            "date": e.date,
            "participants": [
                {"name": p.name, "status": p.status.value}
                for p in e.participants
            ]
        }
        data.append(event_info)
    filename = "export_event_data.json"
    save_to_file(filename, data)
    return filename
