import requests
from flask import Flask, jsonify


def get_air_quality():
    key = "fe3b8e29-ae0f-4fdd-abc4-9ed1e45efffc"
    url = f'http://api.airvisual.com/v2/city?city=Warsaw&state=Mazovia&country=Poland&key={key}'
    response = requests.get(url)
    data = response.json()
    print(data)


get_air_quality()
