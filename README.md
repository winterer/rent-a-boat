# Rent-a-Boat API

A FastAPI-based REST API for managing boat rentals, availability, and related resources. This application provides endpoints to browse and retrieve boat information for a boat rental service.

## 🚢 Features

- **Boat Management**: Browse and retrieve boat information
- **RESTful API**: Clean and intuitive REST endpoints
- **Type Safety**: Full type annotations with Pydantic models
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation
- **Modern Python**: Built with Python 3.13+ and FastAPI

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- **Package Manager**: [uv](https://github.com/astral-sh/uv) - Ultra-fast Python package installer and resolver
- **Language**: Python 3.13+
- **Code Quality**: [Ruff](https://github.com/astral-sh/ruff) - Fast Python linter and formatter

## 📋 Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## 🚀 Quick Start

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rent-a-boat
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Run the application**:
   ```bash
   uv run rentaboat
   ```

   Or using FastAPI directly:
   ```bash
   uv run fastapi dev src/rentaboat/main.py
   ```

4. **Access the API**:
   - API Root: http://localhost:8000
   - Interactive API Documentation: http://localhost:8000/docs
   - Alternative API Documentation: http://localhost:8000/redoc

## 📚 API Documentation

### Endpoints

#### Root Endpoint
- **GET** `/` - Welcome message and API status

#### Boats
- **GET** `/boats` - Retrieve all available boats
- **GET** `/boats/{boat_id}` - Retrieve a specific boat by UUID

### Data Models

#### Boat Model
```json
{
  "id": "uuid4",
  "name": "string",
  "type": "sailing" | "motor" | "row",
  "manufacturer": "string",
  "model": "string",
  "year": 2020,
  "price_per_week": 1000.0
}
```

### Example Responses

#### Get All Boats
```bash
curl http://localhost:8000/boats
```

Response:
```json
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "name": "Rowboat",
    "type": "row",
    "manufacturer": "Acme Corp",
    "model": "Rowing",
    "year": 2020,
    "price_per_week": 500.0
  },
  {
    "id": "987fcdeb-51a2-43d1-9f12-345678901234",
    "name": "Yacht",
    "type": "sailing",
    "manufacturer": "Luxury Yachts Inc.",
    "model": "Sailing",
    "year": 2021,
    "price_per_week": 25000.0
  }
]
```

#### Get Specific Boat
```bash
curl http://localhost:8000/boats/123e4567-e89b-12d3-a456-426614174000
```

Response:
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "Rowboat",
  "type": "row",
  "manufacturer": "Acme Corp",
  "model": "Rowing",
  "year": 2020,
  "price_per_week": 500.0
}
```

## 📁 Project Structure

```
rent-a-boat/
├── src/
│   └── rentaboat/
│       ├── __init__.py
│       ├── main.py              # FastAPI application entry point
│       ├── dependencies.py      # Shared dependencies (currently empty)
│       └── routers/
│           ├── __init__.py
│           └── boats.py         # Boat-related endpoints and models
├── pyproject.toml              # Project configuration and dependencies
├── uv.lock                     # Lock file for reproducible installs
└── README.md                   # This file
```

## 🧪 Development

### Code Quality

The project uses Ruff for linting and formatting with a line length of 120 characters.

```bash
# Run linting
uv run ruff check

# Format code
uv run ruff format
```

### Interactive Development

For development with auto-reload:

```bash
uv run fastapi dev src/rentaboat/main.py
```

This will start the development server with automatic reloading when files change.

## 📝 Configuration

### Environment Variables

Currently, the application runs with default settings. Future versions may include configurable options through environment variables.

### Database

The current implementation uses an in-memory fake database for demonstration purposes. In a production environment, you would replace this with a proper database implementation.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the terms specified in the project configuration.

## 👨‍💻 Author

**Mario Winterer** - mario.winterer@scch.at

## 🔮 Future Enhancements

- [ ] Database integration (PostgreSQL/SQLite)
- [ ] User authentication and authorization
- [ ] Booking/reservation system
- [ ] Payment integration
- [ ] Real-time availability tracking
- [ ] Image upload for boats
- [ ] Search and filtering capabilities
- [ ] Comprehensive test suite
- [ ] Docker containerization
- [ ] CI/CD pipeline
