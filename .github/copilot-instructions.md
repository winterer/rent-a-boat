# Rent-a-Boat AI Development Guide

## Project Overview
This is a FastAPI-based boat rental API using modern Python 3.13+ features with `uv` for dependency management. The codebase follows a modular router-based architecture with in-memory data storage (currently using fake databases).

## Architecture Patterns

### Router-Based API Structure
- **Main app**: `src/rentaboat/main.py` - FastAPI app with router inclusion
- **Routers**: `src/rentaboat/routers/` - Domain-specific API endpoints (e.g., `boats.py`)
- **Dependencies**: `src/rentaboat/dependencies.py` - Shared dependency injection (currently empty but reserved for DB connections, auth, etc.)

### Data Models
- Use Pydantic models with type hints for request/response validation
- Follow pattern in `boats.py`: `BaseModel` with `Field()` descriptors for API documentation
- Type aliases for constrained values: `type BoatType = Literal["sailing", "motor", "row"]`

### Fake Database Pattern
Current implementation uses in-memory lists as fake databases (see `fake_boats_db` in `boats.py`). When extending:
- Use `list[ModelClass]` for collections
- Generate UUIDs with `uuid4()` for IDs
- Implement CRUD with list comprehensions and `next()` for lookups

## Development Workflow

### Essential Commands
```bash
# Install/sync dependencies
uv sync

# Start development server with hot reload
uv run fastapi dev src/rentaboat/main.py

# Run application in production mode
uv run python -m rentaboat

# Access interactive API docs at http://localhost:8000/docs
```

### Adding New Features
1. **New API endpoints**: Create router in `src/rentaboat/routers/`
2. **Include router**: Add to `main.py` with `app.include_router()`
3. **Models**: Define Pydantic models with proper Field descriptions
4. **Fake data**: Create module-level fake database lists

## Code Conventions

### FastAPI Router Setup
```python
router = APIRouter(
    prefix="/resource",
    tags=["resource"],
    responses={404: {"description": "Not found"}},
)
```

### Model Definitions
- Use descriptive `Field()` parameters for auto-generated API docs
- Default factories for UUIDs: `id: UUID = Field(default_factory=uuid4)`
- Type hints with modern Python syntax (union types, generics)

### Error Handling
- Use `HTTPException` for standard HTTP errors
- Pattern: `next()` with `None` default, then check and raise 404

## Project Configuration
- **Package management**: `uv` with `pyproject.toml`
- **Python version**: >=3.13 (uses modern type syntax)
- **Linting**: Ruff configured with 120 character line length
- **Entry point**: `rentaboat = "rentaboat:main"` script in pyproject.toml

## Current Limitations & Extension Points
- **Database**: Currently using in-memory fake databases - ready for SQLAlchemy/async database integration
- **Authentication**: `dependencies.py` is empty but positioned for auth dependencies
- **Testing**: No test structure yet - can add pytest with FastAPI test client
- **Environment config**: No environment variable handling - ready for pydantic-settings

When implementing database integration, replace fake database patterns with async database calls while maintaining the same router and model structure.
