# models/vendor.py
from pydantic import BaseModel

class Vendor(BaseModel):
    name: str
    service: str
    contact: str