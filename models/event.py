from typing import List
from models.participant import Participant

class Event:
    def __init__(self, title: str, location: str, date: str):
        self.title = title
        self.location = location
        self.date = date
        self.participants: List[Participant] = []

    def add_participant(self, participant: Participant):
        self.participants.append(participant)