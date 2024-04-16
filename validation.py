import datetime
from pydantic import BaseModel
from typing import Any


class Args(BaseModel):
    city: str
    state: str
    country: str


def validate_data(data):
    current_timestamp = datetime.datetime.now()

    if data is None:
        return False

    processed_data = {
        'timestamp': current_timestamp,
        "pollution": data["data"]["current"]["pollution"],
        "weather": data["data"]["current"]["weather"],
    }

    weather_data = processed_data["weather"]

    if weather_data["tp"] > 150 or weather_data["pr"] > 2000 or weather_data["ws"] > 1000000:
        return False
    else:
        return processed_data
