# Expense-ledger

## Overview
This is an expense-ledger backend system. It stores the expenses of users and provides CRUD operations on them. The system supports user registration, login, and JWT-based authentication.
This backend system is made robust against errors and maintains data integrity and user privacy. 

## Problem Solved
- In the digital payment ecosystem (UPI/ wallet) user often loses track of spending. This Backend System helps user maintaining budget awareness by recording and organzing expenses.  

## Features
- User registration
- Expense CRUD  operations  
- JWT authentication with expiry

### Technical choices
- SQL -> PostgreSQL
- language -> Python (Cpython 3.11.14)
- Web frameworks -> FastAPI
- API format -> JSON (default in FastAPI)

### Libraries required

#### Built-In libraries
- typing
- os

#### External libraries
- fastapi
- jose
- passlib
- pydantic 
- sqlalchemy

## Request Flow
``` text
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

## Request Lifecycle
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



## Planned improvements
- Refresh tokens addition 
- Adding authorization.
- Frontend Integration.
- Multi-user data isolation and access control





