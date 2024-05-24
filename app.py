from flask import Flask, jsonify
from flask.views import MethodView
from dotenv import load_dotenv
from persistence import DataPersistence
from controllers import WeatherDataController
from client.my_client import get_from_api
from validation import validate_data
import os

load_dotenv()

app = Flask(__name__)

persistency = DataPersistence()
weather_controller = WeatherDataController(
    validate_func=validate_data, persistency=persistency)


class PollutionDataView(MethodView):
    def __init__(self, controller, persistency):
        self.controller = controller
        self.persistency = persistency

    def get(self):
        persisted_data = self.persistency.get_data()
        if persisted_data:
            return jsonify(persisted_data), 200
        else:
            return self.post()

    def post(self):
        api_data = self._fetch_api_data()
        if api_data:
            self.controller.add_data_to_persistency(api_data)
            data = self.persistency.get_data()
            return jsonify(data), 200
        else:
            return jsonify({"error": "Haha, u are stupid!"}), 500

    def _fetch_api_data(self):
        key = os.getenv("API_KEY")
        city = "Warsaw"
        state = "Mazovia"
        country = "Poland"
        return get_from_api(city, state, country, key)


def create_pollution_data_view():
    view = PollutionDataView.as_view(
        'weather', controller=weather_controller, persistency=persistency)
    return view


app.add_url_rule(
    '/weather', view_func=create_pollution_data_view(), methods=["GET", "POST"])

if __name__ == '__main__':
    app.run()
