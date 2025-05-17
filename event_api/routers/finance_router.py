# routers/finance_router.py
from fastapi import APIRouter, status
from models.finance import FinanceRecord, FinanceType
from typing import List

router = APIRouter()
finances: List[FinanceRecord] = []

@router.post("/", response_model=FinanceRecord, status_code=status.HTTP_201_CREATED)
def add_record(record: FinanceRecord):
    finances.append(record)
    return record

@router.get("/summary")
def finance_summary():
    income = sum(r.amount for r in finances if r.type == FinanceType.INCOME)
    expense = sum(r.amount for r in finances if r.type == FinanceType.EXPENSE)
    saldo = income - expense
    return {
        "total_income": income,
        "total_expense": expense,
        "saldo": saldo
    }

@router.get("/", response_model=List[FinanceRecord])
def list_finance():
    return finances
