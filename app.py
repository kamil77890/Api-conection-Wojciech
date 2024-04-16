from flask import Flask, jsonify
from flask.views import MethodView
from dotenv import load_dotenv
from client.my_client import get_from_api
from persistence import DataPersistence
from controllers import WeatherDataController
import datetime
import os

app = Flask(__name__)


class PollutionDataView(MethodView):
    def __init__(self):
        self.p = DataPersistence()
        self.controller = WeatherDataController()

    def get(self):
        load_dotenv()
        key = os.getenv("API_KEY")

        city = "Warsaw"
        state = "Mazovia"
        country = "Poland"

        api_data = get_from_api(
            city, state, country, key)

        if api_data is None:
            print("not good :()")
        else:
            self.controller.add_data_to_persistency(api_data, self.p)
            return jsonify(api_data)


app.add_url_rule('/weather', view_func=PollutionDataView.as_view('weather'))

if __name__ == '__main__':
    app.run()
