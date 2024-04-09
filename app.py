from flask import Flask, jsonify
from backend import DataPersistence, validate_data
from client.my_client import get_cites

app = Flask(__name__)

persistence = DataPersistence()


@app.route("/")
def getting_date():
    data = validate_data("Warsaw")
    if data:
        persistence.store_data(data)
        return jsonify(data)
    else:
        return jsonify({"Nie ma danych, pernie api się wywaliło ;)"}), 404


@app.route("/data")
def all_data():
    data = persistence.get_data()
    return jsonify(data)


@app.route("/city")
def cites_data():
    data = get_cites()
    if data:
        return jsonify(data)
    else:
        return jsonify({"Nie ma danych, pernie api się wywaliło ;)"}), 404


@app.route("/city/<string:param>")
def get_data_for_all_bigger_cities_in_Mazovia(param):
    city = param
    data = validate_data(city)
    if data:
        return jsonify(data)
    else:
        return jsonify({"Nie ma danych, pernie api się wywaliło ;)"}), 404


if __name__ == "__main__":
    app.run(debug=True)
