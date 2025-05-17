# models/event.py
from typing import List
from datetime import date
from models.participant import Participant
from pydantic import BaseModel, Field

class Event(BaseModel):
    title: str
    location: str
    date: date
    participants: List[Participant] = Field(default_factory=list) 