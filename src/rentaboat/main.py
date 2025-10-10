"""This module is the main entry point for the Rent-a-Boat application."""
from fastapi import FastAPI

from .routers import boats

app = FastAPI()


app.include_router(boats.router)


@app.get("/")
async def root():
    """Returns a welcome message for the root endpoint.

    Returns:
        A dictionary with a welcome message.
    """
    return {"message": "Hello from Rent-a-Boat!"}
