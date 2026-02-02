from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import date

# Properly structures the API request instead of just taking any value
class UserCreate(BaseModel):
    email: str
    password: str

class ExpenseCreate(BaseModel):
    amount: condecimal(gt=0)
    category: str
    description: Optional[str] = None
    expense_date: date
