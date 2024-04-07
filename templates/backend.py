from client.my_client import get_air_quality_for_warsaw

import datetime


def walidating():
    data = get_air_quality_for_warsaw()
    current_timestamp = datetime.datetime.now()
    processed_data = {
        'timestamp': current_timestamp,
        'data': data
    }
    # walidacja hehe
    for key, values in processed_data.items():
        if values == current_timestamp:
            print("Jestem bogiem :) !")
            persistence(processed_data)
            return processed_data


def persistence(current_data):
    date = [current_data]
    return date
