"""
Main entry point for the Rent-a-Boat FastAPI application.

This module initializes the FastAPI app, includes routers for different resources,
and defines the root endpoint.
"""

from fastapi import FastAPI

from .routers import boats

app = FastAPI(
    title="Rent-a-Boat API",
    description="API for managing boat rentals, availability, and related resources.",
    version="1.0.0",
)


app.include_router(boats.router)


@app.get("/")
async def root():
    """
    Root endpoint for Rent-a-Boat API.

    Returns a welcome message indicating the API is running.
    """
    return {"message": "Hello from Rent-a-Boat!"}
