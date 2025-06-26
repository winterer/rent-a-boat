# Boat Rental API

A simple FastAPI application to manage boat rentals. This API allows users to list available boats, search for specific types of boats, and manage boat inventory.

## Features

*   **List all boats:** Get a comprehensive list of all boats in the system.
*   **Get boat details:** Retrieve detailed information for a specific boat by its ID.
*   **Create new boats:** Add new boats to the inventory.
*   **Update boat information:** Modify details of existing boats.
*   **Delete boats:** Remove boats from the inventory.
*   **Search boats:** Filter boats based on criteria such as type, maximum price, and availability.

## Tech Stack

*   **FastAPI:** For building the REST API.
*   **Pydantic:** For data validation and settings management.
*   **Uvicorn:** ASGI server to run the application.
*   **HTTPX:** For asynchronous HTTP requests in tests.
*   **Pytest:** For running automated tests.
*   **In-memory "database":** For storing data during runtime (for demonstration purposes).

## Getting Started

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    # git clone <repository-url>
    # cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the development server:

```bash
uvicorn main:app --reload
```

The API will be accessible at `http://127.0.0.1:8000`.

You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs` and alternative documentation (ReDoc) at `http://127.0.0.1:8000/redoc`.

### Running Tests

To run the automated tests:

```bash
pytest
```

This command will discover and run all tests located in `test_main.py`. Ensure you have installed the development dependencies (including `pytest` and `httpx`), which are listed in `requirements.txt`.

## API Endpoints

The main endpoints provided are:

*   `GET /`: Welcome message.
*   `POST /boats/`: Create a new boat.
*   `GET /boats/`: List all boats.
*   `GET /boats/search/`: Search for boats with query parameters:
    *   `boat_type` (string, optional)
    *   `max_price` (float, optional)
    *   `is_available` (boolean, optional)
*   `GET /boats/{boat_id}`: Get details of a specific boat.
*   `PUT /boats/{boat_id}`: Update a specific boat.
*   `DELETE /boats/{boat_id}`: Delete a specific boat.

Refer to the `/docs` endpoint for detailed request/response schemas and to try out the API.

## Project Structure

```
.
├── main.py           # FastAPI application, API endpoints
├── models.py         # Pydantic models for data validation
├── database.py       # In-memory database and helper functions
├── test_main.py      # Pytest tests for the API
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── AGENTS.md         # Instructions for AI agents working on this codebase
```

## Future Enhancements

*   Integration with a persistent relational or NoSQL database.
*   User authentication and authorization.
*   More advanced search and filtering capabilities.
*   Pagination for listing boats.
*   Deployment using Docker and a cloud service.
```
