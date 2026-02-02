from sqlalchemy import create_engine
import os
# Here DB is connected to the python logic
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    future=True
)
