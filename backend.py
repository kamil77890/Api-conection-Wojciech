# backend.py

import datetime
from client.my_client import get_air_quality_for_warsaw


class DataPersistence:
    def __init__(self):
        self.data_store = []
        print(self.data_store)

    def store_data(self, data):
        if self._validate_data(data):
            self.data_store.append(data)
            return True
        else:
            return False

    def get_data(self):
        return self.data_store

    def get_closest_data(self, timestamp):
        closest_data = None
        closest_time_difference = float('inf')
        for data in self.data_store:
            time_difference = abs(
                (data['timestamp'] - timestamp).total_seconds())
            if time_difference < closest_time_difference:
                closest_data = data
                closest_time_difference = time_difference
        return closest_data


def validate_data():
    data = get_air_quality_for_warsaw()
    current_timestamp = datetime.datetime.now()
    processed_data = {
        'timestamp': current_timestamp,
        'data': data["data"]
    }

    required_pollution_fields = ['ts', 'aqius', 'maincn', 'mainus']
    for field in required_pollution_fields:
        if field not in processed_data['data']['current']['pollution']:
            print(processed_data['data']['current']['pollution'])
            return False

        return processed_data


if __name__ == "__main__":
    persistence = DataPersistence()
