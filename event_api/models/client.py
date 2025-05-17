# models/client.py
from pydantic import BaseModel

class Client(BaseModel):
    name: str
    contact: str
    address: str
