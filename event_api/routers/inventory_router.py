# routers/inventory_router.py
from fastapi import APIRouter, status
from models.inventory import InventoryItem
from typing import List

router = APIRouter()
inventories: List[InventoryItem] = []

@router.post("/", response_model=InventoryItem, status_code=status.HTTP_201_CREATED)
def add_inventory(item: InventoryItem):
    inventories.append(item)
    return item

@router.get("/", response_model=List[InventoryItem])
def list_inventory():
    return inventories