# Rent-a-Boat

A modern boat rental platform API built with FastAPI that allows users to browse, book, and manage boat rentals.

## Features

- Browse available boats with detailed information
- Search and filter boats by location, type, and availability
- User authentication and profile management
- Booking system with calendar integration
- Payment processing
- Review and rating system
- Responsive design for mobile and desktop

## Tech Stack

- **Backend**: Python with FastAPI
- **Package Management**: uv
- **Python Version**: >=3.13

## Getting Started

### Prerequisites

- Python 3.13 or higher
- uv package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd rent-a-boat
```

2. Install dependencies:
```bash
uv sync
```

3. Run the development server:
```bash
uv run fastapi dev src/rentaboat/main.py
```

The API will be available at `http://localhost:8000`

## Scripts

- `uv run fastapi dev src/rentaboat/main.py` - Start development server
- `uv run python -m rentaboat` - Run the application
- `uv sync` - Install/update dependencies

## Project Structure

```
rent-a-boat/
├── src/
│   └── rentaboat/          # Main application package
│       ├── __init__.py
│       ├── main.py         # FastAPI application entry point
│       ├── dependencies.py # Dependency injection
│       └── routers/        # API route modules
│           ├── __init__.py
│           └── boats.py    # Boat-related endpoints
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Dependency lock file
└── README.md              # Project documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [your-email@example.com](mailto:your-email@example.com)
