import requests
from flask import Flask, jsonify
from backend import walidating

app = Flask(__name__)


@app.route("/ja")
def getting_date():
    return walidating()


if __name__ == "__main__":
    app.run(debug=True)
