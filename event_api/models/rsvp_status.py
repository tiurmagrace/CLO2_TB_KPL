# models/rsvp_status.py
from enum import Enum

class RSVPStatus(str, Enum):
    ATTENDING = "Hadir"
    NOT_ATTENDING = "Tidak Hadir"
    PENDING = "Belum Dikonfirmasi"