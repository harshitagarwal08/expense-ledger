from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from app.database import engine
from app.auth.hashing import verify_password
from app.auth.jwt import create_access_token

router = APIRouter()

# main would route the client request here
@router.post("/login")
def login(email: str, password: str):
    query = text("""
        SELECT id, password_hash FROM users
        WHERE email = :email
    """)
    # by using with, query execution is isolated
    with engine.connect() as conn:
        user = conn.execute(query, {"email": email}).fetchone()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # JWT is created
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}
