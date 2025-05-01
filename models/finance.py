class FinanceRecord:
    def __init__(self, description: str, amount: float, type: str):
        self.description = description
        self.amount = amount
        self.type = type  # Income or Expense