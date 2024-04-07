from client.my_client import get_air_quality_for_warsaw
import datetime
import json


class DataPersistence:
    def __init__(self):
        self.data_store = {}

    def store_data(self, timestamp, data):
        self.data_store["all_data"] = data, timestamp
        print("store_data" + ''.join(str(item)
              for item in self.data_store["all_data"]))

    def get_data(self):
        return self.data_store.get("all_data", None)

    def upgrate_data(self):
        data = walidating()
        self.store_data(data["timestamp"], data["data"])


def walidating():
    data = get_air_quality_for_warsaw()
    current_timestamp = datetime.datetime.now()
    processed_data = {
        'timestamp': current_timestamp,
        'data': data
    }

    for key, value in processed_data.items():
        if value == current_timestamp:
            print("Poprawne dane!")

    return processed_data


persistence = DataPersistence()
persistence.upgrate_data()
