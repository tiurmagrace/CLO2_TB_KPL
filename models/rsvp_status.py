from enum import Enum

class RSVPStatus(Enum):
    ATTENDING = "Hadir"
    NOT_ATTENDING = "Tidak Hadir"
    UNCONFIRMED = "Belum Konfirmasi"
