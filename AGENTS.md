## Agent Instructions for Boat Rental API

Welcome, agent! This document provides guidelines for working on the Boat Rental API codebase.

### Project Overview

This is a FastAPI application providing a REST API for managing boat rentals. It uses an in-memory database (`database.py`) for simplicity, Pydantic models (`models.py`) for data validation, and `pytest` for testing (`test_main.py`).

### Development Guidelines

1.  **Models (`models.py`):**
    *   When adding or modifying boat attributes, ensure Pydantic models are updated.
    *   Use descriptive field names and appropriate data types.
    *   Include `Field` validations (e.g., `min_length`, `gt`) where applicable.
    *   Update `Config.schema_extra` examples if you change the model structure.

2.  **Database (`database.py`):**
    *   Currently uses an in-memory dictionary. For new CRUD operations, add corresponding helper functions here.
    *   If this were a production app, this module would be replaced with a proper database integration (e.g., SQLAlchemy with PostgreSQL).

3.  **API Endpoints (`main.py`):**
    *   Follow RESTful principles for new endpoints.
    *   Use appropriate HTTP status codes.
    *   Ensure request and response bodies are validated using Pydantic models.
    *   Add OpenAPI documentation (docstrings, `Query`, `Path` descriptions).

4.  **Testing (`test_main.py`):**
    *   **Write tests for all new features and bug fixes.**
    *   Use `pytest` and `httpx.AsyncClient`.
    *   Ensure tests cover:
        *   Happy paths (successful operations).
        *   Edge cases.
        *   Error handling (e.g., invalid input, resource not found).
    *   The `clear_and_repopulate_db` fixture resets the database for each test. Add any new globally required test data there or within specific test setup.
    *   Run tests using the command: `pytest`

5.  **Dependencies:**
    *   Add any new dependencies to `requirements.txt`.

6.  **Code Style:**
    *   Follow PEP 8 guidelines for Python code.
    *   Keep lines under a reasonable length (e.g., 100-120 characters).
    *   Use clear and concise variable and function names.

### Running the Application

1.  Install dependencies: `pip install -r requirements.txt`
2.  Run the development server: `uvicorn main:app --reload`
    The API will be available at `http://127.0.0.1:8000`.
    Interactive API documentation (Swagger UI) will be at `http://127.0.0.1:8000/docs`.

### Future Considerations (If expanding the project)

*   **Database:** Migrate to a persistent database (e.g., PostgreSQL, SQLite).
*   **Authentication & Authorization:** Implement user accounts and roles.
*   **More Complex Search/Filtering:** Enhance search capabilities.
*   **Deployment:** Containerize with Docker, deploy to a cloud platform.
*   **Background Tasks:** For operations like sending notifications.

Please ensure all tests pass before submitting changes. Good luck!
