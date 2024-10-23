from flask import Flask, jsonify, request
from weather_processor import store_weather_data, calculate_daily_summary
from weather_fetcher import get_weather_data
from alert_system import check_thresholds

app = Flask(__name__)

@app.route('/fetch_weather', methods=['GET'])
def fetch_weather():
    weather_data = get_weather_data()
    store_weather_data(weather_data)

    for city, data in weather_data.items():
        check_thresholds(city, data['temp'], data['main'])

    return jsonify(weather_data)

@app.route('/daily_summary', methods=['GET'])
def daily_summary():
    calculate_daily_summary()
    return jsonify({"message": "Daily summary calculated"})

if __name__ == '__main__':
    app.run(debug=True)
