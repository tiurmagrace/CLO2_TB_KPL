# models/inventory.py
from pydantic import BaseModel

class InventoryItem(BaseModel):
    name: str
    jumlah: int
    status: str = "Tersedia"