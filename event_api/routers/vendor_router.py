# routers/vendor_router.py
from fastapi import APIRouter, status
from models.vendor import Vendor
from typing import List

router = APIRouter()
vendors: List[Vendor] = []

@router.post("/", response_model=Vendor, status_code=status.HTTP_201_CREATED)
def add_vendor(vendor: Vendor):
    vendors.append(vendor)
    return vendor

@router.get("/", response_model=List[Vendor])
def list_vendors():
    return vendors