# Copilot Instructions for Rent-a-Boat API

## Architecture Overview

This is a **FastAPI-based microservice** using the router pattern with **modern Python 3.13+** and **uv** package management. The application follows a clean separation between business logic (routers) and application setup (main.py).

**Key architectural decisions:**
- **Modular router design**: Each domain (boats, future: users, bookings) gets its own router in `src/rentaboat/routers/`
- **In-memory data store**: Currently uses `fake_boats_db` list for simplicity - this is the **primary data layer**
- **Type-first approach**: Heavy use of Pydantic models and Python 3.13 type hints including `type` aliases

## Development Workflow

### Essential Commands (not in README)
```bash
# Development server with auto-reload (primary development command)
uv run fastapi dev src/rentaboat/main.py

# Production-style server
uv run fastapi run src/rentaboat/main.py

# Console entry point (different from web server)
uv run rentaboat  # Runs __init__.py main() - just prints hello

# Code quality (configured for 120 char line length)
uv run ruff check
uv run ruff format
```

### Project Structure Patterns

**Follow these conventions when adding features:**

1. **New endpoints**: Add to existing router in `src/rentaboat/routers/` or create new router
2. **Models**: Define Pydantic models in the same file as endpoints (see `boats.py`)
3. **Router registration**: Import and include router in `main.py` using `app.include_router()`
4. **Type definitions**: Use Python 3.13 `type` aliases for Union types (e.g., `type BoatType = Literal[...]`)

### Data Layer Pattern

**Critical**: The app uses in-memory storage with specific patterns:

```python
# Global module-level list serves as database
fake_boats_db: list[Boat] = [...]

# CRUD operations use list comprehensions and next()
boat = next((boat for boat in fake_boats_db if boat.id == boat_id), None)
```

When extending data operations, maintain this pattern or replace entirely with proper database.

## Router Configuration Pattern

**Standard router setup** (copy this pattern for new domains):

```python
router = APIRouter(
    prefix="/domain",           # URL prefix
    tags=["domain"],           # OpenAPI grouping  
    responses={404: {"description": "Not found"}},  # Common responses
)
```

## Pydantic Model Conventions

**Field patterns used in this codebase:**

```python
class ModelName(BaseModel):
    id: UUID = Field(default_factory=uuid4)  # Auto-generated UUIDs
    name: str = Field(description="...")      # Always include descriptions
    optional_field: str = Field(default="")  # Use explicit defaults
    numeric_field: float = Field(default=1000.0, description="...")
```

## Development Environment

- **Ruff**: Primary linter/formatter (120 char line length)
- **VS Code**: Pre-configured with format-on-save and Ruff as default formatter
- **Python 3.13**: Uses modern syntax including `type` aliases
- **uv**: Package manager - use `uv run` for all commands, not `python` directly

When adding dependencies, use `uv add <package>`.

## API Design Patterns

**Endpoint naming**: 
- Collection: `GET /boats/` returns list
- Item: `GET /boats/{id}` returns single item  
- Use UUID path parameters, not query strings for identification

**Error handling**: Use `HTTPException` with appropriate status codes (see 404 pattern in boats.py)

## Testing & Debugging

**No test suite exists yet** - when adding tests, place in `tests/` directory and use pytest.

**Debugging**: Use FastAPI's automatic OpenAPI docs at `/docs` - this is the primary API exploration tool.
