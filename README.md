# Rent-a-Boat

A simple FastAPI application to manage a boat rental service.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.13+
* [uv](https://github.com/astral-sh/uv)

### Installation

1. Clone the repository:
   ```bash
   git clone https://your-repository-url.com/rentaboat.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rentaboat
   ```
3. Install the dependencies:
   ```bash
   uv pip install -e .
   ```

## Usage

To run the application, use the following command:

```bash
uvicorn src.rentaboat.main:app --reload
```

## API Endpoints

The following endpoints are available:

* `GET /`: Returns a welcome message.
* `GET /boats`: Returns a list of all available boats.
* `GET /boats/{boat_id}`: Returns a specific boat by its ID.
