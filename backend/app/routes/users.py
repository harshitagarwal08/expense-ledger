from fastapi import APIRouter
from app.database import engine
from app.schemas import UserCreate
from app.crud.users import create_user
from app.auth.jwt import create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    with engine.begin() as conn:
        user_id = create_user(conn, user.email, user.password)
    return {
        "user_id": user_id,
        "token": create_access_token(user_id)
    }
