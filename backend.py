import datetime
from client.my_client import get_air_quality_for_warsaw


class DataPersistence:
    def __init__(self):
        self.data_store = []
        print(self.data_store)

    def store_data(self, data):
        if data:
            self.data_store.append(data)
            return True
        else:
            return False

    def get_data(self):
        return self.data_store


def validate_data():
    data = get_air_quality_for_warsaw()
    current_timestamp = datetime.datetime.now()
    processed_data = {
        'timestamp': current_timestamp,
        'data': data["data"]
    }

    required_fields = ['ts', 'aqius', 'maincn', 'mainus']
    for field in required_fields:
        if field not in processed_data['data']['current']['pollution']:
            return False
        else:
            persistence = DataPersistence()
            persistence.store_data(processed_data)

            return processed_data


if __name__ == "__main__":
    persistence = DataPersistence()
    persistence.store_data(validate_data())
