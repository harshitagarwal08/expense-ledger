from datetime import datetime, timedelta
from jose import jwt
import os
from dotenv import load_dotenv

# JWT helps maintain integrity and
# reduces the need to look at DB each time a request comes
# helps in scaling the system.
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY not set")
ALGORITHM = "HS256"


def create_access_token(user_id: int):
    payload = {"sub": user_id, "exp": datetime.utcnow() + timedelta(hours=2)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
