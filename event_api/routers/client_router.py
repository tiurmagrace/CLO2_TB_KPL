# routers/client_router.py
from fastapi import APIRouter, HTTPException, status
from models.client import Client
from typing import List

router = APIRouter()
clients: List[Client] = []

@router.post("/", response_model=Client, status_code=status.HTTP_201_CREATED)
def add_client(client: Client):
    clients.append(client)
    return client

@router.get("/", response_model=List[Client])
def list_clients():
    return clients