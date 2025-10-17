"""The main application file for the Rent-a-Boat API."""
from fastapi import FastAPI

from .routers import boats

app = FastAPI()


app.include_router(boats.router)


@app.get("/")
async def root():
    """Returns a welcome message."""
    return {"message": "Hello from Rent-a-Boat!"}
