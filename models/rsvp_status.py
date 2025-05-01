from enum import Enum

class RSVPStatus(Enum):
    UNCONFIRMED = "Belum Dikonfirmasi"
    ATTENDING = "Hadir"
    NOT_ATTENDING = "Tidak Hadir"