from fastapi import APIRouter, Depends
from app.database import engine
from app.schemas import ExpenseCreate
from app.crud.expenses import create_expense, list_expenses
from app.auth.dependencies import get_current_user

router = APIRouter()

@router.post("/expenses")
def add_expense(
    expense: ExpenseCreate,
    user_id: int = Depends(get_current_user)
):
    with engine.begin() as conn: #begin implements transaction preserving database correctness when error occurs
        expense_id = create_expense(conn, user_id, expense.dict())
    return {"id": expense_id}


@router.get("/expenses")
def get_expenses(
    user_id: int = Depends(get_current_user)
):
    with engine.connect() as conn:
        return list_expenses(conn, user_id)
