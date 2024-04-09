import requests


def get_cites():
    key = "fe3b8e29-ae0f-4fdd-abc4-9ed1e45efffc"
    url = f'http://api.airvisual.com/v2/cities?state=Mazovia&country=Poland&key={key}'
    response = requests.get(url)
    data = response.json()
    return data["data"]


def get_air_quality(city):
    cities = get_cites()
    for dict_city in cities:
        for k, v in dict_city.items():
            if v == city:
                print("działa")
                key = "fe3b8e29-ae0f-4fdd-abc4-9ed1e45efffc"
                url = f'http://api.airvisual.com/v2/city?city={city}&state=Mazovia&country=Poland&key={key}'
                response = requests.get(url)
                data = response.json()
                return data
