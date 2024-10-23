# Weather Monitoring System with Rollups and Aggregates

## Description
A real-time data processing system that monitors weather conditions using the OpenWeatherMap API and provides daily rollups and aggregate data.

## Setup Instructions

1. Install dependencies:
    ```
    pip install Flask requests plotly
    ```

2. Initialize the database:
    ```
    python weather_processor.py
    ```

3. Run the application:
    ```
    python app.py
    ```

4. Access the API at `http://127.0.0.1:5000/`.

## Features

- **Real-time Weather Data**: Continuously fetch weather data for 6 Indian cities.
- **Daily Summaries**: Calculate daily aggregates for temperature and dominant weather condition.
- **Alerts**: Trigger alerts based on user-defined thresholds.
- **Visualization**: Visualize weather trends with temperature plots.

## API Endpoints

- `GET /fetch_weather`: Fetch and store weather data.
- `GET /daily_summary`: Calculate daily weather summaries.
