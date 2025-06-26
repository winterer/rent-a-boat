from typing import List, Dict
import uuid
from models import Boat # Assuming models.py is in the same directory or accessible via PYTHONPATH

# In-memory "database"
# In a real application, this would be replaced with a proper database (e.g., PostgreSQL, MongoDB)
# and an ORM or database driver (e.g., SQLAlchemy, Motor).
db: Dict[uuid.UUID, Boat] = {}

def _generate_initial_boats():
    initial_boats_data = [
        {"name": "Sea Breeze", "type": "Sailboat", "price_per_hour": 100.00, "is_available": True},
        {"name": "WaveRunner X", "type": "Jet Ski", "price_per_hour": 65.00, "is_available": True},
        {"name": "Coastal Cruiser", "type": "Motorboat", "price_per_hour": 150.00, "is_available": False},
        {"name": "River Explorer", "type": "Kayak", "price_per_hour": 25.00, "is_available": True},
        {"name": "Ocean Master", "type": "Yacht", "price_per_hour": 500.00, "is_available": True},
        {"name": "Lake Hopper", "type": "Pontoon Boat", "price_per_hour": 80.00, "is_available": False},
        {"name": "Speed Demon", "type": "Speedboat", "price_per_hour": 120.00, "is_available": True},
        {"name": "Tranquil Paddler", "type": "Canoe", "price_per_hour": 30.00, "is_available": True},
        {"name": "Fishing Buddy", "type": "Fishing Boat", "price_per_hour": 90.00, "is_available": True},
        {"name": "Luxury Liner", "type": "Catamaran", "price_per_hour": 350.00, "is_available": False},
    ]
    for boat_data in initial_boats_data:
        boat = Boat(**boat_data)
        db[boat.id] = boat

_generate_initial_boats()

# Functions to interact with the "database"
async def get_all_boats() -> List[Boat]:
    return list(db.values())

async def get_boat_by_id(boat_id: uuid.UUID) -> Boat | None:
    return db.get(boat_id)

async def create_boat(boat_data: Boat) -> Boat:
    # In a real scenario, you might want to ensure the ID isn't already taken,
    # though with UUIDs, collisions are extremely rare.
    # For BoatCreate model, we assign a new ID here.
    if boat_data.id in db:
        # This case should ideally not happen if IDs are generated on creation
        # and not passed in by the client for new boats.
        # Consider how to handle ID generation if client can suggest one.
        raise ValueError("Boat with this ID already exists")
    db[boat_data.id] = boat_data
    return boat_data

async def update_boat_in_db(boat_id: uuid.UUID, boat_update_data: Dict) -> Boat | None:
    existing_boat = db.get(boat_id)
    if not existing_boat:
        return None

    updated_boat_data = existing_boat.dict()
    updated_boat_data.update(boat_update_data)

    # Pydantic models are immutable by default, so we create a new instance
    db[boat_id] = Boat(**updated_boat_data)
    return db[boat_id]

async def delete_boat_from_db(boat_id: uuid.UUID) -> Boat | None:
    return db.pop(boat_id, None)

# Example: Get a list of boats (this would typically be called from your API endpoints)
# async def main():
#     all_boats = await get_all_boats()
#     print(f"Found {len(all_boats)} boats:")
#     for boat in all_boats:
#         print(f"- {boat.name} ({boat.type}): ${boat.price_per_hour}/hr, Available: {boat.is_available}, ID: {boat.id}")

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())
