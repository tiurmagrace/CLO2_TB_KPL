# models/finance.py
from enum import Enum
from pydantic import BaseModel

class FinanceType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class FinanceRecord(BaseModel):
    description: str
    amount: float
    type: FinanceType