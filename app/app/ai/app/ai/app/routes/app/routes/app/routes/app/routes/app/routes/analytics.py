from fastapi import APIRouter
import random
import datetime
from app.ai.ibm_granite import ask_ibm_granite

router = APIRouter()

@router.get("/analytics")
def get_health_analytics():
    days = 7
    today = datetime.date.today()

    data = {
        "heart_rate": [],
        "blood_pressure": [],
        "glucose": [],
        "dates": []
    }

    for i in range(days):
        date = (today - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        data["dates"].append(date)
        data["heart_rate"].append(random.randint(65, 90))
        data["blood_pressure"].append({
            "systolic": random.randint(110, 130),
            "diastolic": random.randint(70, 85)
        })
        data["glucose"].append(random.randint(85, 120))

    # Generate AI insight summary
    prompt = (
        "Analyze the following weekly patient data:\n"
        f"Heart Rate: {data['heart_rate']}\n"
        f"Blood Pressure: {data['blood_pressure']}\n"
        f"Glucose: {data['glucose']}\n"
        "Provide a summary of trends and any health concerns."
    )
    insights = ask_ibm_granite(prompt)

    return {
        "data": data,
        "insights": insights
    }
