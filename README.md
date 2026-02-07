# Expense-ledger

![Python](https://img.shields.io/badge/python-3.11.14-blue)
![FastAPI](https://img.shields.io/badge/fastapi-0.100.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## Overview

This is an expense-ledger RESTful API backend system. It stores the expenses of users and provides CRUD operations on them. The system supports user registration, login, and JWT-based authentication.
This backend system is made robust against errors and maintains data integrity and user privacy.

## Problem Solved

- In the digital payment ecosystem (UPI/ wallet) user often loses track of spending. This Backend System helps user maintaining budget awareness by recording and organizing expenses.

## Features

- User registration
- Expense CRUD operations
- JWT authentication with expiry

## Technical choices

- SQL -> PostgreSQL >= 15
- language -> Python (Cpython 3.11.14)
- Web frameworks -> FastAPI >= 0.100
- API format -> JSON (default in FastAPI)

## Libraries required

### Built-In libraries

- typing
- os
- datetime

### External libraries

- dotenv
- fastapi
- jose
- passlib
- pydantic
- sqlalchemy

## Folder Structure

```text
expense-ledger
├── backend
│ ├── app
│ │ ├── auth
│ │ │ ├── dependencies.py
│ │ │ ├── hashing.py
│ │ │ └── jwt.py
│ │ ├── crud
│ │ │ ├── expenses.py
│ │ │ └── users.py
│ │ ├── database.py
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── routes
│ │ │ ├── auth.py
│ │ │ ├── expenses.py
│ │ │ └── users.py
│ │ └── schemas.py
│ └── REQUIREMENTS.txt
├── database
│ └── schema.sql
├── frontend
└── README.md
```

## Environment Variables

- Create a .env file in the project root:
- DATABASE_URL=postgresql://postgres:<password>@localhost/expense_ledger
- SECRET_KEY=<your_super_secret_random_string>

- DATABASE_URL: PostgreSQL connection URL
- SECRET_KEY: JWT signing key (never push to GitHub)

## Request Flow

```text
Client
  ↓
HTTP Request (JSON)
  ↓
ASGI Server (Uvicorn)
  ↓
FastAPI Application
  ↓
Router → Dependency Injection
  ↓
Pydantic Validation
  ↓
Business Logic
  ↓
Database connection (via SQLAlchemy engine)
  ↓
Database (PostgreSQL)
  ↓
Response (JSON)
```

### Request Lifecycle

1. Client

- Client sends HTTP requests (via Swagger UI, frontend, or API client).
- Requests contain JSON payloads and JWT tokens (if authenticated).

2. ASGI Server (Uvicorn)

- Uvicorn receives the HTTP request.
- Forwards it to the FastAPI application.

3. FastAPI Routing:

- FastAPI matches the request URL and HTTP method to a route.
- Dependencies (JWT verification, DB session) are resolved.

4. Input Validation:

- Pydantic schemas validate and parse request data.
- Invalid data is rejected before business logic runs.

5. Business Logic:

- Route-specific logic executes:
- Authentication
- Authorization
- Expense creation / retrieval / update / deletion

6. Database Interaction:

- SQLAlchemy ORM generates parameterized SQL queries.
- PostgreSQL enforces constraints and transactions.

7. Response:

- Result is converted to a Pydantic response model.
- JSON response is sent back to the client.

## Architecture

### Security

- Hashed Passwords via passlib
- .env for system password and System data
- Parameterized queries (SQL injection prevention)
- JWT for stateless authentication(identity verification)

### Data integrity

- Transactions
- Modular and isolated code

### Reliability

- Strict validation using Pydantic.
- Constraints enforced at the database level

## Run locally

- conda activate finance_tracker
- pip install -r requirements.txt
- uvicorn main:app --reload

## REST API Endpoints

| Method | Endpoint         | Auth | Description                 | Query Params                  |
| :----: | ---------------- | :--: | --------------------------- | ----------------------------- |
|  POST  | `/register`      |  No  | Register a new user         | -                             |
|  POST  | `/login`         |  No  | Authenticate user & get JWT | -                             |
|  POST  | `/expenses`      | Yes  | Create a new expense        | -                             |
|  GET   | `/expenses`      | Yes  | Retrieve all expenses       | `limit` (int), `offset` (int) |
|  PUT   | `/expenses/{id}` | Yes  | Update an expense           | -                             |
| DELETE | `/expenses/{id}` | Yes  | Delete an expense           | -                             |

## API DOCS

- Swagger UI: http://127.0.0.1:8000/docs

## Naming Conventions (Backend / Python / FastAPI)

| Category          | Convention             | Example            | Reason                  |
| ----------------- | ---------------------- | ------------------ | ----------------------- |
| Variables         | `snake_case`           | `total_amount`     | Python standard (PEP 8) |
| Functions         | `snake_case`           | `get_expenses()`   | Action-oriented         |
| Classes           | `PascalCase`           | `Expense`, `User`  | Represents entities     |
| Constants         | `UPPER_SNAKE_CASE`     | `SECRET_KEY`       | Signals immutability    |
| Python files      | `snake_case.py`        | `database.py`      | Import-friendly         |
| Folders           | `snake_case/`          | `auth_utils/`      | Clean imports           |
| API routes        | lowercase nouns        | `/expenses/{id}`   | RESTful design          |
| Route handlers    | verb + noun            | `create_expense()` | Maps to HTTP verbs      |
| DB tables         | plural `snake_case`    | `expenses`         | Collection semantics    |
| DB columns        | `snake_case`           | `created_at`       | SQL standard            |
| Foreign keys      | `<table>_id`           | `user_id`          | Clear relationships     |
| SQLAlchemy models | Singular `PascalCase`  | `Expense`          | Conceptual entity       |
| `__tablename__`   | plural `snake_case`    | `"expenses"`       | DB alignment            |
| Pydantic schemas  | `PascalCase + Purpose` | `ExpenseCreate`    | Explicit intent         |
| JWT fields        | standard claims        | `sub`, `exp`       | Interoperability        |
| Env variables     | `UPPER_SNAKE_CASE`     | `DATABASE_URL`     | OS convention           |

## Accepted Tradeoffs

- JWT tokens can be reused on a user’s device until expiry
- Users may submit meaningless or dummy data
- System might experience temporary downtime (backups exist)
- Database autosave not immediate; transactions maintain integrity

## Planned Improvements

- Implement refresh tokens
- Add role-based authorization
- Frontend integration with React/Vue/Flutter
