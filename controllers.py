from validation import validate_data
from persistence import DataPersistence

persistency = DataPersistence()


class WeatherDataController:
    def __init__(self):
        pass

    def add_data_to_persistency(self, data: dict, persistency) -> bool:
        if validate_data(data):
            persistency.store_data(data)
            return True
        else:
            return False


