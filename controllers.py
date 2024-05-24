from validation import validate_data
from persistence import DataPersistence

persistency = DataPersistence()

# wstrzykiwanie zależności dp innita {'' DONE :) ''}


class WeatherDataController:
    def __init__(self, validate_func, persistency):
        self.validate_func = validate_func
        self.persistency = persistency

    def add_data_to_persistency(self, data):
        validated_data = self.validate_func(data)
        if validated_data:
            self.persistency.store_data(validated_data)
            return True
        else:
            return False
