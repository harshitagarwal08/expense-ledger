from sqlalchemy import text
from app.auth.hashing import hash_password

# inserts user credentials to system DB
def create_user(conn, email, password):
    query = text("""
        INSERT INTO users (email, password_hash)
        VALUES (:email, :password)
        RETURNING id
    """)
    result = conn.execute(query, {
        "email": email,
        "password": hash_password(password)
    })
    return result.scalar()
