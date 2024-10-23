import sqlite3

# Function to check and trigger alerts if thresholds are breached
def check_thresholds(city, temp, main_condition, temp_threshold=35):
    if temp > temp_threshold:
        print(f"ALERT: Temperature exceeded {temp_threshold}°C in {city}! Current temp: {temp}°C")
    
    # Add more conditions for alerts if necessary
