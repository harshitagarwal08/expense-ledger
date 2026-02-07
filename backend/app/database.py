from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Here DB is connected to the python logic
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL, future=True)
