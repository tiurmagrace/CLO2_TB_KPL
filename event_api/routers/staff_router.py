# routers/staff_router.py
from fastapi import APIRouter, status
from models.staff import Staff
from typing import List

router = APIRouter()
staffs: List[Staff] = []

@router.post("/", response_model=Staff, status_code=status.HTTP_201_CREATED)
def add_staff(staff: Staff):
    staffs.append(staff)
    return staff

@router.get("/", response_model=List[Staff])
def list_staff():
    return staffs