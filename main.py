from fastapi import FastAPI

app = FastAPI(
    title="Boat Rental API",
    description="A simple API to list and search for boats available for rent.",
    version="0.1.0",
)

from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
import uuid

from models import Boat, BoatCreate, BoatUpdate # Assuming models.py is in the same directory
import database # Assuming database.py is in the same directory

app = FastAPI(
    title="Boat Rental API",
    description="A simple API to list and search for boats available for rent.",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Boat Rental API! See /docs for API documentation."}

# --- Boat Endpoints ---

@app.post("/boats/", response_model=Boat, status_code=201)
async def create_new_boat(boat_create: BoatCreate):
    """
    Create a new boat.
    - **name**: Name of the boat (required)
    - **type**: Type of boat (e.g., Sailboat, Motorboat) (required)
    - **price_per_hour**: Rental price per hour (required)
    - **is_available**: Availability status (optional, defaults to True)
    """
    boat = Boat(**boat_create.dict(), id=uuid.uuid4()) # Generate ID here
    return await database.create_boat(boat)

@app.get("/boats/", response_model=List[Boat])
async def list_all_boats():
    """
    Retrieve a list of all boats.
    """
    return await database.get_all_boats()

@app.get("/boats/search/", response_model=List[Boat])
async def search_boats(
    boat_type: Optional[str] = Query(None, description="Filter by boat type (e.g., Sailboat, Kayak)"),
    max_price: Optional[float] = Query(None, gt=0, description="Filter by maximum price per hour"),
    is_available: Optional[bool] = Query(None, description="Filter by availability status")
):
    """
    Search for boats based on specified criteria.
    - **boat_type**: Exact match for boat type (case-sensitive).
    - **max_price**: Boats with price_per_hour less than or equal to this value.
    - **is_available**: True to find available boats, False for unavailable.
    """
    all_boats = await database.get_all_boats()
    filtered_boats = []

    for boat in all_boats:
        match = True
        if boat_type is not None and boat.type != boat_type:
            match = False
        if max_price is not None and boat.price_per_hour > max_price:
            match = False
        if is_available is not None and boat.is_available != is_available:
            match = False

        if match:
            filtered_boats.append(boat)

    if not filtered_boats and any([boat_type, max_price, is_available]):
        # Return empty list if filters are active but no boats match
        return []
    elif not filtered_boats and not any([boat_type, max_price, is_available]):
        # This case means the database itself is empty
        return []

    return filtered_boats

@app.get("/boats/{boat_id}", response_model=Boat)
async def get_boat_details(boat_id: uuid.UUID):
    """
    Retrieve details for a specific boat by its ID.
    """
    boat = await database.get_boat_by_id(boat_id)
    if not boat:
        raise HTTPException(status_code=404, detail=f"Boat with ID {boat_id} not found")
    return boat

@app.put("/boats/{boat_id}", response_model=Boat)
async def update_existing_boat(boat_id: uuid.UUID, boat_update: BoatUpdate):
    """
    Update details for an existing boat.
    Provide only the fields you want to change.
    """
    boat_data_to_update = boat_update.dict(exclude_unset=True)
    if not boat_data_to_update:
        raise HTTPException(status_code=400, detail="No update data provided")

    updated_boat = await database.update_boat_in_db(boat_id, boat_data_to_update)
    if not updated_boat:
        raise HTTPException(status_code=404, detail=f"Boat with ID {boat_id} not found for update")
    return updated_boat

@app.delete("/boats/{boat_id}", status_code=204)
async def delete_existing_boat(boat_id: uuid.UUID):
    """
    Delete a boat by its ID.
    Returns 204 No Content on successful deletion.
    """
    deleted_boat = await database.delete_boat_from_db(boat_id)
    if not deleted_boat:
        raise HTTPException(status_code=404, detail=f"Boat with ID {boat_id} not found for deletion")
    return None # FastAPI will return 204 No Content
