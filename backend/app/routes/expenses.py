from datetime import date
from typing import Optional
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query

from app.database import engine
from app.schemas import ExpenseCreate
from app.crud.expenses import (
    create_expense,
    list_expenses,
    get_expense,
    update_expense,
    delete_expense,
)
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.post("/expenses")
def add_expense(expense: ExpenseCreate, user_id: int = Depends(get_current_user)):
    with engine.begin() as conn:  # begin implements transaction preserving database correctness when error occurs
        expense_id = create_expense(conn, user_id, expense.dict())
    return {"id": expense_id}


@router.get("/expenses")
def get_expenses(
    user_id: int = Depends(get_current_user),
    category: Optional[str] = Query(default=None),
    from_date: Optional[date] = Query(default=None),
    to_date: Optional[date] = Query(default=None),
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    """
    Returns paginated list of expenses for the current user.
    - limit: max items per page (1-100)
    - offset: number of items to skip
    """
    with engine.connect() as conn:
        return list_expenses(conn, user_id, limit=limit, offset=offset)


@router.get("/expenses/{expense_id}")
def get_single_expense(expense_id: int, user_id: int = Depends(get_current_user)):
    with engine.connect() as conn:
        expense = get_expense(conn, user_id, expense_id)

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


@router.put("/expenses/{expense_id}")
def replace_expense(
    expense_id: int, expense: ExpenseCreate, user_id: int = Depends(get_current_user)
):
    with engine.begin() as conn:
        updated_id = update_expense(conn, user_id, expense_id, expense.dict())

    if not updated_id:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"id": updated_id}


@router.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int, user_id: int = Depends(get_current_user)):
    with engine.begin() as conn:
        deleted_id = delete_expense(conn, user_id, expense_id)

    if not deleted_id:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"deleted": True}
