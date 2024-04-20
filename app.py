from flask import Flask, jsonify
from flask.views import MethodView
from dotenv import load_dotenv
from persistence import DataPersistence
from controllers import WeatherDataController
from client.my_client import get_from_api
import os

app = Flask(__name__)

persistency = DataPersistence()


class PollutionDataView(MethodView):
    def __init__(self):
        self.controller = WeatherDataController()

    def get(self):
        persisted_data = persistency.get_data()
        if persisted_data:
            return jsonify(persisted_data), 200
        else:
            self.post()

    def post(self):
        api_data = self._fetch_api_data()
        if api_data:
            self.controller.add_data_to_persistency(api_data, persistency)
            data = persistency.get_data()
            return jsonify(data), 200
        else:
            return jsonify({"error": "Failed to fetch data from API"}), 500

    def _fetch_api_data(self):
        load_dotenv()
        key = os.getenv("API_KEY")
        city = "Warsaw"
        state = "Mazovia"
        country = "Poland"
        return get_from_api(city, state, country, key)


app.add_url_rule('/weather', view_func=PollutionDataView.as_view('weather'))

if __name__ == '__main__':
    app.run()
