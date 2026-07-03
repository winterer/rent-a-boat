# Rent-a-Boat

Rent-a-Boat is a FastAPI-based web application for managing boat rentals.

## Features

- RESTful API to manage boats using FastAPI.
- Endpoints to list all available boats and fetch specific boat details.
- Pydantic models for data validation.

## Requirements

- Python 3.13 or newer
- `uv` for dependency management

## Installation

To set up the project locally:

1. Clone the repository.
2. Ensure you have `uv` installed. If not, follow the [uv installation guide](https://github.com/astral-sh/uv).
3. Install the dependencies:

```bash
uv sync
```

Or add dependencies using:
```bash
uv add <package>
```

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn src.rentaboat.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Development

- **Formatting/Linting:** The project uses `ruff` with a configured line length of 120 characters.
- **Testing:** The project currently does not have a test suite.
