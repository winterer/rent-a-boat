import pytest
from httpx import AsyncClient
from fastapi import status
import uuid

# Make sure the main app can be imported.
# This might require setting PYTHONPATH or adjusting project structure if tests are in a subfolder.
# For this example, assuming main.py is in the same directory or accessible.
from main import app
from models import Boat
import database # To access the in-memory db for setup/teardown or direct inspection

# Global variable to store a boat ID created during tests for use in other tests
created_boat_id: uuid.UUID = None
# Global variable to store a sample boat for comparison
sample_boat_data = {"name": "Test Boat", "type": "UnitTest", "price_per_hour": 50.0, "is_available": True}


@pytest.fixture(scope="session")
def event_loop():
    """Overrides pytest-asyncio default event_loop fixture to enable session scope."""
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        yield ac

@pytest.fixture(autouse=True, scope="function")
@pytest.mark.asyncio # Explicitly mark this autouse async fixture
async def clear_and_repopulate_db():
    """Fixture to clear and repopulate the database before each test function."""
    database.db.clear()
    database._generate_initial_boats() # Repopulate with initial set for consistent testing environment
    # Add one specific boat for testing GET by ID, PUT, DELETE
    global created_boat_id
    boat_to_create = Boat(**sample_boat_data)
    created_boat = await database.create_boat(boat_to_create)
    created_boat_id = created_boat.id


@pytest.mark.asyncio
async def test_read_root(client: AsyncClient):
    response = await client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Welcome to the Boat Rental API! See /docs for API documentation."}

@pytest.mark.asyncio
async def test_create_new_boat(client: AsyncClient):
    global created_boat_id # We'll assign to this global to use the ID in other tests
    payload = {"name": "Voyager", "type": "Speedboat", "price_per_hour": 120.50, "is_available": True}
    response = await client.post("/boats/", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["type"] == payload["type"]
    assert data["price_per_hour"] == payload["price_per_hour"]
    assert data["is_available"] == payload["is_available"]
    assert "id" in data
    # Store this ID if you want to use it in subsequent tests (e.g., get, update, delete)
    # For this test suite, the fixture `clear_and_repopulate_db` adds a known boat.
    # created_boat_id = uuid.UUID(data["id"])


@pytest.mark.asyncio
async def test_list_all_boats(client: AsyncClient):
    response = await client.get("/boats/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    # The db is repopulated with 10 initial boats + 1 sample boat by the fixture
    assert len(data) == 11
    # Check if one of the boats is the one we expect (e.g., from _generate_initial_boats or the one added in fixture)
    # This assumes 'created_boat_id' is set by a fixture or a previous test that adds a known boat.
    # Let's find the boat added by the fixture.
    assert any(boat['id'] == str(created_boat_id) for boat in data)


@pytest.mark.asyncio
async def test_get_boat_details(client: AsyncClient):
    assert created_boat_id is not None, "created_boat_id was not set by fixture"
    response = await client.get(f"/boats/{created_boat_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == str(created_boat_id)
    assert data["name"] == sample_boat_data["name"]
    assert data["type"] == sample_boat_data["type"]

@pytest.mark.asyncio
async def test_get_boat_details_not_found(client: AsyncClient):
    non_existent_id = uuid.uuid4()
    response = await client.get(f"/boats/{non_existent_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Boat with ID {non_existent_id} not found"}

@pytest.mark.asyncio
async def test_update_existing_boat(client: AsyncClient):
    assert created_boat_id is not None, "created_boat_id was not set by fixture"
    update_payload = {"name": "Updated Test Boat Name", "price_per_hour": 99.99, "is_available": False}
    response = await client.put(f"/boats/{created_boat_id}", json=update_payload)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == str(created_boat_id)
    assert data["name"] == update_payload["name"]
    assert data["price_per_hour"] == update_payload["price_per_hour"]
    assert data["is_available"] == update_payload["is_available"]
    # Type should remain unchanged
    assert data["type"] == sample_boat_data["type"]

@pytest.mark.asyncio
async def test_update_boat_not_found(client: AsyncClient):
    non_existent_id = uuid.uuid4()
    update_payload = {"name": "Ghost Boat"}
    response = await client.put(f"/boats/{non_existent_id}", json=update_payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.asyncio
async def test_update_boat_no_data(client: AsyncClient):
    assert created_boat_id is not None, "created_boat_id was not set by fixture"
    response = await client.put(f"/boats/{created_boat_id}", json={})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "No update data provided"}


@pytest.mark.asyncio
async def test_delete_existing_boat(client: AsyncClient):
    assert created_boat_id is not None, "created_boat_id was not set by fixture"
    response = await client.delete(f"/boats/{created_boat_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify it's actually deleted
    get_response = await client.get(f"/boats/{created_boat_id}")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.asyncio
async def test_delete_boat_not_found(client: AsyncClient):
    non_existent_id = uuid.uuid4()
    response = await client.delete(f"/boats/{non_existent_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

# --- Search Endpoint Tests ---

@pytest.mark.asyncio
async def test_search_boats_by_type(client: AsyncClient):
    # One of the initial boats is "Sailboat"
    response = await client.get("/boats/search/?boat_type=Sailboat")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0 # Expect at least one
    for boat in data:
        assert boat["type"] == "Sailboat"
    # The sample boat added by fixture is "UnitTest"
    response_unittest = await client.get("/boats/search/?boat_type=UnitTest")
    assert response_unittest.status_code == status.HTTP_200_OK
    data_unittest = response_unittest.json()
    assert len(data_unittest) == 1
    assert data_unittest[0]["name"] == sample_boat_data["name"]


@pytest.mark.asyncio
async def test_search_boats_by_max_price(client: AsyncClient):
    # Price of sample_boat_data is 50.0
    response = await client.get("/boats/search/?max_price=50.0")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    found_sample_boat = False
    for boat in data:
        assert boat["price_per_hour"] <= 50.0
        if boat["id"] == str(created_boat_id):
            found_sample_boat = True
    assert found_sample_boat, "The sample boat should be included in results for max_price=50.0"

    response_lower = await client.get("/boats/search/?max_price=20.0") # No initial boat is this cheap
    assert response_lower.status_code == status.HTTP_200_OK
    data_lower = response_lower.json()
    assert data_lower == []


@pytest.mark.asyncio
async def test_search_boats_by_availability(client: AsyncClient):
    # sample_boat_data is_available=True
    response_available = await client.get("/boats/search/?is_available=true")
    assert response_available.status_code == status.HTTP_200_OK
    data_available = response_available.json()
    assert isinstance(data_available, list)
    assert len(data_available) > 0
    found_sample_boat_available = False
    for boat in data_available:
        assert boat["is_available"] is True
        if boat["id"] == str(created_boat_id):
            found_sample_boat_available = True
    assert found_sample_boat_available

    # Make the sample boat unavailable and test
    await client.put(f"/boats/{created_boat_id}", json={"is_available": False})

    response_unavailable = await client.get("/boats/search/?is_available=false")
    assert response_unavailable.status_code == status.HTTP_200_OK
    data_unavailable = response_unavailable.json()
    assert isinstance(data_unavailable, list)
    assert len(data_unavailable) > 0
    found_sample_boat_unavailable = False
    for boat in data_unavailable:
        assert boat["is_available"] is False
        if boat["id"] == str(created_boat_id): # The sample boat should now be here
            found_sample_boat_unavailable = True
    assert found_sample_boat_unavailable


@pytest.mark.asyncio
async def test_search_boats_combined_filters(client: AsyncClient):
    # Search for the specific test boat created by the fixture
    response = await client.get(f"/boats/search/?boat_type={sample_boat_data['type']}&max_price={sample_boat_data['price_per_hour']}&is_available={str(sample_boat_data['is_available']).lower()}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == str(created_boat_id)
    assert data[0]["name"] == sample_boat_data["name"]

@pytest.mark.asyncio
async def test_search_boats_no_results(client: AsyncClient):
    response = await client.get("/boats/search/?boat_type=NonExistentType&max_price=10")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

@pytest.mark.asyncio
async def test_search_boats_no_filters(client: AsyncClient):
    # Should return all boats (10 initial + 1 sample)
    response = await client.get("/boats/search/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 11

@pytest.mark.asyncio
async def test_create_boat_invalid_data(client: AsyncClient):
    # Missing required fields (e.g., name)
    payload = {"type": "Kayak", "price_per_hour": 20.0}
    response = await client.post("/boats/", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Invalid price (e.g., negative)
    payload_invalid_price = {"name": "Sinker", "type": "Submarine", "price_per_hour": -10.0}
    response_invalid_price = await client.post("/boats/", json=payload_invalid_price)
    assert response_invalid_price.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    # Check for specific error detail if Pydantic provides it (FastAPI wraps it)
    # Example: error_detail = response_invalid_price.json()["detail"][0]
    # assert error_detail["loc"] == ["body", "price_per_hour"]
    # assert "must be greater than 0" in error_detail["msg"] # Pydantic v1 style, v2 might differ slightly

@pytest.mark.asyncio
async def test_update_boat_invalid_data(client: AsyncClient):
    assert created_boat_id is not None
    # Invalid price (e.g., zero or negative)
    payload = {"price_per_hour": 0}
    response = await client.put(f"/boats/{created_boat_id}", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    # detail = response.json()["detail"][0]
    # assert detail["loc"] == ["body", "price_per_hour"]
    # assert "must be greater than 0" in detail["msg"]

# Note: To run these tests, you'd typically use `pytest` in your terminal.
# Ensure httpx, pytest, and pytest-asyncio are installed.
# pip install pytest pytest-asyncio httpx
# The `event_loop` fixture is for `pytest-asyncio` compatibility across different scopes.
# The `clear_and_repopulate_db` fixture ensures a clean state for each test,
# which is good for test isolation but might be slow for very large initial datasets.
# For larger applications, you might use a separate test database.
