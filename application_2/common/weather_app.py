import requests
import time

API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# List of metro cities with their city IDs
CITIES = {
    "Delhi": 1273294,
    "Mumbai": 1275339,
    "Chennai": 1264527,
    "Bangalore": 1277333,
    "Kolkata": 1275004,
    "Hyderabad": 1269843
}

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to fetch weather data for a city
def fetch_weather(city_id):
    url = f"{BASE_URL}?id={city_id}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to fetch and process weather for all cities
def get_weather_data():
    weather_data = {}
    for city, city_id in CITIES.items():
        data = fetch_weather(city_id)
        if data:
            weather_data[city] = {
                'main': data['weather'][0]['main'],
                'temp': kelvin_to_celsius(data['main']['temp']),
                'feels_like': kelvin_to_celsius(data['main']['feels_like']),
                'dt': data['dt']
            }
    return weather_data
