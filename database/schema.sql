CREATE TABLE
    expenses (
        id SERIAL PRIMARY KEY,
        amount NUMERIC(10, 2) NOT NULL CHECK (amount > 0),
        category TEXT NOT NULL,
        description TEXT,
        expense_date DATE NOT NULL DEFAULT CURRENT_DATE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    );