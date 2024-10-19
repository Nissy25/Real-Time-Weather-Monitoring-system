import requests
import pandas as pd
import time
import sqlite3
import os
from datetime import datetime

# Configuration
API_KEY = 'f405d227bde5d372dbd6ba386f3e530a'  # Replace with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
DB_NAME = 'weather_data.db'
UPDATE_INTERVAL = 300  # Update every 5 minutes

# Create a database connection
def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            date TEXT,
            temp REAL,
            feels_like REAL,
            weather TEXT
        )
    ''')
    conn.commit()
    return conn

# Fetch weather data from OpenWeatherMap
def fetch_weather(city):
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    return response.json()

# Process and store weather data
def process_weather_data(conn, data):
    city = data['name']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    weather = data['weather'][0]['main']
    date = datetime.fromtimestamp(data['dt']).date()
    
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, date, temp, feels_like, weather)
        VALUES (?, ?, ?, ?, ?)
    ''', (city, date, temp, feels_like, weather))
    conn.commit()

# Daily summary calculation
def calculate_daily_summary(conn):
    query = '''
        SELECT date, 
               city, 
               AVG(temp) AS avg_temp, 
               MAX(temp) AS max_temp, 
               MIN(temp) AS min_temp,
               MAX(weather) AS dominant_weather
        FROM weather
        GROUP BY date, city
    '''
    summary_df = pd.read_sql(query, conn)
    print(summary_df)

# Main function
def main():
    conn = create_db()
    try:
        while True:
            for city in CITIES:
                weather_data = fetch_weather(city)
                process_weather_data(conn, weather_data)
            calculate_daily_summary(conn)
            time.sleep(UPDATE_INTERVAL)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    finally:
        conn.close()

if __name__ == '__main__':
    main()
