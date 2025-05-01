from models.rsvp_status import RSVPStatus

class Participant:
    def __init__(self, name: str):
        self.name = name
        self.status = RSVPStatus.UNCONFIRMED