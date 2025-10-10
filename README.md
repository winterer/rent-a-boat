# Rent-a-Boat API

This is a simple FastAPI application for managing a boat rental service.

## Project Description

The Rent-a-Boat API provides endpoints to view available boats for rent. It's built with FastAPI and serves as a demonstration of a basic web API.

## Setup and Installation

To run this project, you'll need Python 3.11 or higher.

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment and install dependencies:**

    We recommend using `uv` to manage dependencies.

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install uv
    uv pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt`, you can install the dependencies from `pyproject.toml`:

    ```bash
    uv pip install .
    ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn src.rentaboat.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

The following API endpoints are available:

*   **`GET /`**: The root endpoint, which returns a welcome message.
*   **`GET /boats`**: Retrieves a list of all available boats.
*   **`GET /boats/{boat_id}`**: Retrieves a specific boat by its unique ID.

You can also access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.