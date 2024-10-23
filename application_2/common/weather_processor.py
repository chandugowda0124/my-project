import sqlite3
from datetime import datetime
from collections import Counter

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY,
            city TEXT,
            main TEXT,
            temp REAL,
            feels_like REAL,
            timestamp INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            id INTEGER PRIMARY KEY,
            city TEXT,
            date TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to store weather data in the database
def store_weather_data(weather_data):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    for city, data in weather_data.items():
        cursor.execute('''
            INSERT INTO weather_data (city, main, temp, feels_like, timestamp) 
            VALUES (?, ?, ?, ?, ?)
        ''', (city, data['main'], data['temp'], data['feels_like'], data['dt']))
    conn.commit()
    conn.close()

# Function to calculate daily rollups
def calculate_daily_summary():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    # Calculate summary for each city
    for city in ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]:
        today = datetime.now().strftime("%Y-%m-%d")
        cursor.execute('''
            SELECT temp, main FROM weather_data 
            WHERE city = ? AND date(timestamp, 'unixepoch') = ?
        ''', (city, today))
        data = cursor.fetchall()

        if data:
            temps = [row[0] for row in data]
            conditions = [row[1] for row in data]
            
            avg_temp = sum(temps) / len(temps)
            max_temp = max(temps)
            min_temp = min(temps)
            dominant_condition = Counter(conditions).most_common(1)[0][0]
            
            cursor.execute('''
                INSERT INTO daily_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (city, today, avg_temp, max_temp, min_temp, dominant_condition))

    conn.commit()
    conn.close()
