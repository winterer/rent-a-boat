# Rent-a-Boat API

This is a simple FastAPI application for managing a boat rental service. It provides API endpoints for listing available boats and retrieving specific boats by their ID.

## Setup

This project uses `uv` for dependency management. To get started, you'll need to have Python 3.13 or higher installed.

1. **Install uv:**

   If you don't have `uv` installed, you can install it with pip:

   ```bash
   pip install uv
   ```

2. **Create a virtual environment:**

   It's recommended to create a virtual environment to isolate the project's dependencies.

   ```bash
   uv venv
   ```

3. **Install dependencies:**

   With the virtual environment activated, install the required dependencies from `pyproject.toml` using `uv`:

   ```bash
   uv pip install -e .
   ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn src.rentaboat.main:app --reload
```

This will start a local development server. You can access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API Endpoints

The following API endpoints are available:

* **`GET /boats`**: Returns a list of all available boats.
* **`GET /boats/{boat_id}`**: Returns a single boat by its unique ID.

### Boat Schema

The `Boat` object has the following structure:

```json
{
  "id": "string (UUID)",
  "name": "string",
  "type": "string (sailing, motor, or row)",
  "manufacturer": "string",
  "model": "string",
  "year": "integer",
  "price_per_week": "number"
}
```