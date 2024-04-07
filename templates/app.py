import requests
from flask import Flask, jsonify
from backend import walidating
from persistence import persistence

app = Flask(__name__)


@app.route("/s")
def getting_date():
    return walidating()


@app.route("/a")
def all_data():
    return persistence()


if __name__ == "__main__":
    app.run(debug=True)
