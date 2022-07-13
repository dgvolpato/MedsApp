from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

class DailyStatus(str, Enum):
    take_pill = "Take Pill"
    good_for_today = "Good for Today"

class PillIntake(BaseModel):
    date: date
    intake: bool

app = FastAPI()


@app.get("/pill-intake")
async def get_pill_intake():
    return {"message": "Hello World"}


@app.post("/pill-intake/{date}")
async def post_pill_intake(date: date):
    pillIntake = PillIntake()
    pillIntake.date = date
    pillIntake.intake = True
    return {pillIntake}


@app.get("/daily-status")
async def get_daily_status():
    return {"message": "Hello World"}


@app.delete("/pill-intake")
async def delete_pill_intake():
    return {"message": "Hello World"}


@app.get("/")
async def root():
    return {"message": "Hello World"}