# Rent-a-Boat

A simple API for managing a boat rental service.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.12+
*   `uv` for dependency management

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/rentaboat.git
    ```
2.  Install the dependencies:
    ```bash
    uv pip install -e .
    ```

## Usage

To run the application, use the following command:

```bash
uvicorn src.rentaboat.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

*   `GET /`: Returns a welcome message.
*   `GET /boats/`: Returns a list of all boats.
*   `GET /boats/{boat_id}`: Returns a specific boat by its ID.

#### Examples

**Get all boats:**

```bash
curl -X 'GET' 'http://127.0.0.1:8000/boats/' -H 'accept: application/json'
```

**Get a specific boat:**

First, get the ID of a boat from the `GET /boats/` endpoint. Then, use that ID to get the boat's details:

```bash
curl -X 'GET' 'http://127.0.0.1:8000/boats/{boat_id}' -H 'accept: application/json'
```