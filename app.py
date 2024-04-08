import requests
import datetime
from flask import Flask, jsonify, render_template
from backend import DataPersistence, validate_data

app = Flask(__name__)

persistence = DataPersistence()


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/s")
def getting_date():
    data = validate_data()
    return jsonify(data)


@app.route("/a")
def all_data():
    data = persistence.get_data()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
