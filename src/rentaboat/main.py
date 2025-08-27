from fastapi import FastAPI

from .routers import boats

app = FastAPI()


app.include_router(boats.router)


@app.get("/")
async def root():
    return {"message": "Hello from Rent-a-Boat!"}
