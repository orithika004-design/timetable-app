from fastapi import FastAPI
from datetime import datetime
from timetable_data import TIMETABLE

app = FastAPI(title="Term 6 Timetable API")

# -----------------------------
# Utility functions
# -----------------------------

def get_today_day():
    return datetime.today().strftime("%A")

def get_current_week():
    today = datetime.today().date()
    for week, data in TIMETABLE.items():
        if data["start"] <= today <= data["end"]:
            return week
    return None

# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Timetable API is live 🚀",
        "endpoints": [
            "/today",
            "/week/{week_number}",
            "/full"
        ]
    }

@app.get("/today")
def today_schedule():
    week = get_current_week()
    day = get_today_day()

    if not week:
        return {"message": "No classes today 🎉"}

    return {
        "week": week,
        "day": day,
        "classes": TIMETABLE[week]["schedule"].get(day, [])
    }

@app.get("/week/{week_number}")
def week_schedule(week_number: int):
    key = f"Week {week_number}"
    if key not in TIMETABLE:
        return {"error": "Invalid week number"}

    return TIMETABLE[key]

@app.get("/full")
def full_timetable():
    return TIMETABLE
