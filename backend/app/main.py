from enum import Enum
from tracemalloc import take_snapshot
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from backend.app.db import database, PillIntake
from fastapi.middleware.cors import CORSMiddleware

class DailyStatus(str, Enum):
    take_pill = "Take Pill"
    good_for_today = "Good for Today"

app = FastAPI(title="MedsApp")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
    "http://localhost:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/pill-intake")
async def get_pill_intake():
    today_string = "{:%m/%d/%Y}".format(datetime.now())
    
    try:
        today_intake = await PillIntake.objects.filter(intake_date=today_string).get()
    except:
        today_intake = await PillIntake.objects.get_or_create(intake_date=today_string, intake=False)
    
    return today_intake


@app.put("/pill-intake")
async def put_pill_intake():
    today_string = "{:%m/%d/%Y}".format(datetime.now())

    try:
        today_intake = await PillIntake.objects.filter(intake_date=today_string).get()
        today_intake.intake = True
        await today_intake.update()
    except:
        today_intake = await PillIntake.objects.get_or_create(intake_date=today_string, intake=True)
    return today_intake


@app.get("/daily-status")
async def get_daily_status():

    today_intake = await get_pill_intake()

    if today_intake.intake == True:
        return {"status" : DailyStatus.good_for_today}
    else:
        return {"status" : DailyStatus.take_pill}


@app.delete("/pill-intake")
async def delete_pill_intake():
    today_string = "{:%m/%d/%Y}".format(datetime.now())
    try:
        today_intake = await PillIntake.objects.delete(intake_date=today_string)
    except:
        today_intake = {}

    return today_intake


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()