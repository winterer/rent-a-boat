"""
Boats router module for the Rent-a-Boat API.

This module provides REST endpoints for managing boat inventory, including
listing all boats and retrieving individual boat details. Currently uses
an in-memory data store for simplicity.

The router handles three types of boats: sailing, motor, and row boats.
"""

from typing import Literal
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/boats",
    tags=["boats"],
    responses={404: {"description": "Not found"}},
)

type BoatType = Literal["sailing", "motor", "row"]


class Boat(BaseModel):
    """
    Boat model representing a rentable boat in the system.

    This model defines the structure for boat data including identification,
    specifications, and pricing information.

    Attributes:
        id: Unique identifier for the boat (auto-generated UUID)
        name: Display name of the boat
        type: Category of boat (sailing, motor, or row)
        manufacturer: Company that built the boat
        model: Specific model designation
        year: Manufacturing year
        price_per_week: Weekly rental price in currency units
    """

    id: UUID = Field(default_factory=uuid4)
    name: str = Field(description="The name of the boat")
    type: BoatType = Field(description="The type of the boat")
    manufacturer: str = Field(description="The manufacturer of the boat")
    model: str = Field(default="", description="The model of the boat")
    year: int = Field(default=2020, description="The year of the boat")
    price_per_week: float = Field(default=1000.0, description="The price per week of the boat")


fake_boats_db: list[Boat] = [
    Boat(
        id=uuid4(),
        name="Rowboat",
        type="row",
        manufacturer="Acme Corp",
        model="Rowing",
        year=2020,
        price_per_week=500.0,
    ),
    Boat(
        id=uuid4(),
        name="Yacht",
        type="sailing",
        manufacturer="Luxury Yachts Inc.",
        model="Sailing",
        year=2021,
        price_per_week=25000.0,
    ),
]


@router.get("/")
async def read_boats():
    """
    Retrieve all available boats.

    Returns a list of all boats currently in the system inventory.
    This endpoint does not require authentication and provides the complete
    boat catalog for browsing.

    Returns:
        list[Boat]: A list of all boat objects in the database

    Example:
        GET /boats/

        Response:
        [
            {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Rowboat",
                "type": "row",
                "manufacturer": "Acme Corp",
                "model": "Rowing",
                "year": 2020,
                "price_per_week": 500.0
            }
        ]
    """
    return fake_boats_db


@router.get("/{boat_id}")
async def read_boat(boat_id: UUID):
    """
    Retrieve a specific boat by its ID.

    Fetches detailed information for a single boat using its unique identifier.
    Useful for displaying boat details or checking availability before booking.

    Args:
        boat_id (UUID): The unique identifier of the boat to retrieve

    Returns:
        Boat: The boat object with all details

    Raises:
        HTTPException: 404 error if no boat exists with the given ID

    Example:
        GET /boats/123e4567-e89b-12d3-a456-426614174000

        Response:
        {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "name": "Yacht",
            "type": "sailing",
            "manufacturer": "Luxury Yachts Inc.",
            "model": "Sailing",
            "year": 2021,
            "price_per_week": 25000.0
        }
    """
    boat = next((boat for boat in fake_boats_db if boat.id == boat_id), None)
    if boat is None:
        raise HTTPException(status_code=404, detail="Boat not found")
    return boat
