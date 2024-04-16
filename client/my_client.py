import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()


def get_from_api(city, state, country, api_key):
    url = f'http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


# def get_cites(key):
#     url = f'http://api.airvisual.com/v2/cities?state=Mazovia&country=Poland&key={key}'
#     response = requests.get(url)
#     data = response.json()
#     return data["data"]
