from pydantic import BaseModel, Field
from typing import Optional
import uuid

class Boat(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str = Field(..., min_length=1, description="The name of the boat")
    type: str = Field(..., min_length=1, description="The type of boat (e.g., Sailboat, Motorboat, Kayak)")
    price_per_hour: float = Field(..., gt=0, description="The rental price per hour in USD")
    is_available: bool = Field(True, description="Whether the boat is currently available for rent")

    class Config:
        schema_extra = {
            "example": {
                "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                "name": "Sea Serpent",
                "type": "Motorboat",
                "price_per_hour": 75.50,
                "is_available": True
            }
        }

class BoatCreate(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the boat")
    type: str = Field(..., min_length=1, description="The type of boat (e.g., Sailboat, Motorboat, Kayak)")
    price_per_hour: float = Field(..., gt=0, description="The rental price per hour in USD")
    is_available: Optional[bool] = True

    class Config:
        schema_extra = {
            "example": {
                "name": "Wave Rider",
                "type": "Jet Ski",
                "price_per_hour": 50.00,
                "is_available": True
            }
        }

class BoatUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, description="The name of the boat")
    type: Optional[str] = Field(None, min_length=1, description="The type of boat (e.g., Sailboat, Motorboat, Kayak)")
    price_per_hour: Optional[float] = Field(None, gt=0, description="The rental price per hour in USD")
    is_available: Optional[bool] = Field(None, description="Whether the boat is currently available for rent")

    class Config:
        schema_extra = {
            "example": {
                "name": "Ocean Explorer",
                "price_per_hour": 120.00,
                "is_available": False
            }
        }
