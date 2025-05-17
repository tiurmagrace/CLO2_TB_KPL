# models/participant.py
from pydantic import BaseModel
from models.rsvp_status import RSVPStatus

class Participant(BaseModel):
    name: str
    status: RSVPStatus = RSVPStatus.PENDING