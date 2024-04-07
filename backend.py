from client.my_client import get_air_quality_for_warsaw
import datetime


class DataPersistence:
    def __init__(self):
        self.data_store = {}

    def store_data(self, timestamp, data):
        str_timestamp = str(timestamp)
        self.data_store[str_timestamp] = data

    def get_data(self):
        print(self.data_store)
        return self.data_store

    def update_data(self):
        validated_data = self.validate_data()
        if validated_data:
            timestamp = validated_data["timestamp"]
            data = validated_data["data"]
            self.store_data(timestamp, data)
        else:
            print("Failed to update data.")

    def validate_data(self):
        data = get_air_quality_for_warsaw()
        current_timestamp = datetime.datetime.now()
        processed_data = {
            'timestamp': current_timestamp,
            'data': data
        }

        for key, value in processed_data.items():
            if key == 'timestamp' and key == 'data':
                timestamp_value = value
                if timestamp_value == current_timestamp:
                    continue

            elif key == 'data':
                data_value = value
                state = data_value["state"]
                city = data_value["city"]
                country = data_value["country"]
                if state == "Mazovia" and city == "Warsaw" and country == "Poland":
                    return processed_data

        return None


persistence = DataPersistence()
persistence.update_data()
persistence.get_data() 
