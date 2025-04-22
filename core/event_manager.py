from models.event import Event
from models.participant import Participant
from models.rsvp_status import RSVPStatus
from typing import List
import csv
from datetime import datetime

events: List[Event] = []

def tambah_event(title, location, date):
    new_event = Event(title, location, date)
    events.append(new_event)
    return new_event

def tambah_peserta(event_index, name):
    participant = Participant(name)
    events[event_index].add_participant(participant)
    return participant

def atur_rsvp(event_index, participant_name, konfirmasi):
    event = events[event_index]
    for p in event.participants:
        if p.name.lower() == participant_name.lower():
            if konfirmasi == "ya":
                p.status = RSVPStatus.ATTENDING
            elif konfirmasi == "tidak":
                p.status = RSVPStatus.NOT_ATTENDING
            return True
    return False

def export_data():
    filename = f"event_data_{datetime.now().strftime('%Y-%m-%d')}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Judul Event", "Lokasi", "Tanggal", "Nama Peserta", "Status Kehadiran"])
        for event in events:
            if event.participants:
                for p in event.participants:
                    writer.writerow([event.title, event.location, event.date, p.name, p.status.value])
            else:
                writer.writerow([event.title, event.location, event.date, "(tidak ada peserta)", ""])
    return filename
