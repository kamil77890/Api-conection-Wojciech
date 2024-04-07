import requests
import datetime
from flask import Flask, jsonify
from backend import walidating, DataPersistence

app = Flask(__name__)

persistence = DataPersistence()


@app.route("/s")
def getting_date():
    data = walidating()
    return jsonify(data)


@app.route("/a")
def all_data():
    data = persistence.get_data()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
