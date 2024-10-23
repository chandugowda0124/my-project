import sqlite3
import plotly.graph_objs as go

def plot_weather_trends(city):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT temp, datetime(timestamp, 'unixepoch') as timestamp 
        FROM weather_data WHERE city = ? ORDER BY timestamp
    ''', (city,))
    
    data = cursor.fetchall()
    temps = [row[0] for row in data]
    timestamps = [row[1] for row in data]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=temps, mode='lines', name='Temperature'))
    
    fig.update_layout(title=f"Temperature Trends for {city}", xaxis_title='Time', yaxis_title='Temperature (C)')
    fig.show()

plot_weather_trends("Delhi")
