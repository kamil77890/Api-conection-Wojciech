import datetime
from client.my_client import get_air_quality


class DataPersistence:
    def __init__(self):
        self.data_store = []

    def store_data(self, data):
        if data:
            self.data_store.append(data)
            return True
        else:
            return False

    def get_data(self):
        return self.data_store


def validate_data(city):
    data = get_air_quality(city)
    persistence = DataPersistence()
    current_timestamp = datetime.datetime.now()

    if data is None:
        return False

    processed_data = {
        'timestamp': current_timestamp,
        'data': data["data"]
    }

    weater_data = processed_data["data"]["current"]["weather"]

    if weater_data["tp"] > 150 or weater_data["pr"] > 2000 or weater_data["ws"] > 1000000:
        return False
    else:
        persistence.store_data(processed_data)
        return processed_data
