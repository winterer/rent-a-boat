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
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(description="The name of the boat")
    type: BoatType = Field(description="The type of the boat")
    manufacturer: str = Field(description="The manufacturer of the boat")
    model: str = Field(default="", description="The model of the boat")
    year: int = Field(default=2020, description="The year of the boat")
    price_per_week: float = Field(
        default=1000.0, description="The price per week of the boat"
    )


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
async def read_boats(q: str | None = None):
    if q:
        search_results = [
            boat
            for boat in fake_boats_db
            if q.lower()
            in (
                boat.name.lower()
                + boat.type.lower()
                + boat.manufacturer.lower()
                + boat.model.lower()
            )
        ]
        return search_results
    return fake_boats_db


@router.get("/{boat_id}")
async def read_boat(boat_id: UUID):
    boat = next((boat for boat in fake_boats_db if boat.id == boat_id), None)
    if boat is None:
        raise HTTPException(status_code=404, detail="Boat not found")
    return boat
