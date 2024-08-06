from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI()


class Trip(BaseModel):
    id: UUID
    destination: str
    start_date: str
    end_date: str
    description: Optional[str] = None


class CreateTrip(BaseModel):
    destination: str
    start_date: str
    end_date: str
    description: Optional[str] = None


trips = []


@app.post("/trips", response_model=Trip)
async def create_trip(trip: CreateTrip):
    new_trip = Trip(id=uuid4(), **trip.dict())
    trips.append(new_trip)
    return new_trip


@app.get("/trips", response_model=List[Trip])
async def list_trips():
    return trips


@app.get("/trips/{trip_id}", response_model=Trip)
async def get_trip(trip_id: UUID):
    for trip in trips:
        if trip.id == trip_id:
            return trip
    raise HTTPException(status_code=404, detail="Trip not found")


@app.put("/trips/{trip_id}", response_model=Trip)
async def update_trip(trip_id: UUID, updated_trip: CreateTrip):
    for trip in trips:
        if trip.id == trip_id:
            trip.destination = updated_trip.destination
            trip.start_date = updated_trip.start_date
            trip.end_date = updated_trip.end_date
            trip.description = updated_trip.description
            return trip
    raise HTTPException(status_code=404, detail="Trip not found")


@app.delete("/trips/{trip_id}", response_model=Trip)
async def delete_trip(trip_id: UUID):
    for i, trip in enumerate(trips):
        if trip.id == trip_id:
            return trips.pop(i)
    raise HTTPException(status_code=404, detail="Trip not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
