from sqlalchemy import text

# handles the insertion of expenses by a user
def create_expense(conn, user_id, expense):
    query = text("""
        INSERT INTO expenses
        (user_id, amount, category, description, expense_date)
        VALUES
        (:user_id, :amount, :category, :description, :expense_date) #parameters prevent SQL injection attack on my DB
        RETURNING id
    """)
    result = conn.execute(query, {
        "user_id": user_id,
        **expense
    })
    return result.scalar()

# list all expenses of a particular user
def list_expenses(conn, user_id):
    query = text("""
        SELECT * FROM expenses
        WHERE user_id = :user_id
        ORDER BY expense_date DESC
    """)
    result = conn.execute(query, {"user_id": user_id})
    return [dict(row._mapping) for row in result]
