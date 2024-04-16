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
