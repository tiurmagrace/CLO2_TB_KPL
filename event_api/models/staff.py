# models/staff.py
from pydantic import BaseModel

class Staff(BaseModel):
    name: str
    role: str