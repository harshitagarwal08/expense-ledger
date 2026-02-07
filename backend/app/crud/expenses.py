from sqlalchemy import text


# handles the insertion of expenses by a user
def create_expense(conn, user_id, expense):
    query = text(
        """
        INSERT INTO expenses
        (user_id, amount, category, description, expense_date)
        VALUES
        (:user_id, :amount, :category, :description, :expense_date) #parameters prevent SQL injection attack on my DB
        RETURNING id
    """
    )
    result = conn.execute(query, {"user_id": user_id, **expense})
    return result.scalar()


# list all expenses of a particular user
from sqlalchemy import text


def list_expenses(conn, user_id, limit=10, offset=0):
    """
    Fetch expenses for a user with pagination
    """
    query = text(
        """
        SELECT *
        FROM expenses
        WHERE user_id = :user_id
        ORDER BY expense_date DESC
        LIMIT :limit OFFSET :offset
    """
    )
    result = conn.execute(query, {"user_id": user_id, "limit": limit, "offset": offset})
    return [dict(row._mapping) for row in result]


# Gets a particular expense
def get_expense(conn, user_id, expense_id):
    query = text(
        """
        SELECT * FROM expenses
        WHERE id = :expense_id AND user_id = :user_id
    """
    )
    result = conn.execute(
        query, {"expense_id": expense_id, "user_id": user_id}
    ).fetchone()

    return dict(result._mapping) if result else None


# update expense of a particular user
def update_expense(conn, user_id, expense_id, expense):
    query = text(
        """
        UPDATE expenses
        SET amount = :amount,
            category = :category,
            description = :description,
            expense_date = :expense_date
        WHERE id = :user_id AND expense_id = :expense_id
        RETURNING id
    """
    )
    result = conn.execute(
        query, {"expense_id": expense_id, "user_id": user_id, **expense}
    )

    return result.scalar


# Delete a particular expense
def delete_expense(conn, user_id, expense_id):
    query = text(
        """
        DELETE FROM expenses
        WHERE id = :expense_id AND user_id = :user_id
        RETURNING id
    """
    )
    result = conn.execute(query, {"expense_id": expense_id, "user_id": user_id})
    return result.scalar()
