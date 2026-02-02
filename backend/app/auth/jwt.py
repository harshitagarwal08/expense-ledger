from datetime import datetime, timedelta
from jose import jwt
import os
# JWT helps maintain integrity and
# reduces the need to look at DB each time a request comes
# helps in scaling the system.
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(user_id: int):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
