from validation import validate_data
from persistence import DataPersistence

persistency = DataPersistence()


class WeatherDataController:
    def __init__(self):
        pass

    def add_data_to_persistency(self, data: dict, persistency) -> bool:
        validated_data = validate_data(data)
        if validated_data:
            persistency.store_data(validated_data)
            return True
        else:
            return False
