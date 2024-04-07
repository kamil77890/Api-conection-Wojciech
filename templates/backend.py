from templates.client.my_client import get_air_quality_for_warsaw
import datetime


def walidating():
    data = get_air_quality_for_warsaw()
    timestamp = datetime.datetime.now()
    processed_data = {
        'timestamp': timestamp,
        'data': data
    }
    #walidacja hehe
    for city in data:
        if city == "Warsow":
            return processed_data
