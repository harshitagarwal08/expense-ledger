from sqlalchemy import (
    Table, Column, Integer, Text,
    Numeric, Date, ForeignKey, MetaData
)

# To make the future decisions on the system flexible and be able to change SQL
# A schema copy of DB is maintained to make SQL replaceable
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", Text, unique=True, nullable=False),
    Column("password_hash", Text, nullable=False),
)

expenses = Table(
    "expenses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("amount", Numeric(10, 2), nullable=False),
    Column("category", Text, nullable=False),
    Column("description", Text),
    Column("expense_date", Date, nullable=False),
)
