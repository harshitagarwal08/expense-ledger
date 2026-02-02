from fastapi import FastAPI
from app.routes import users, expenses, auth

app = FastAPI(title="Expense Ledger")

# Routes the requests according to request
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(expenses.router)
