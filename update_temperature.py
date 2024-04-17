import requests
import csv
from datetime import datetime
import os

API_KEY = '110bdf4bda55fd77ead07c62c444ab1a'
CITIES = {
    'Paris': {'lat': 48.8566, 'lon': 2.3522},
    'London': {'lat': 51.5074, 'lon': -0.1278},
    'New York City': {'lat': 40.7128, 'lon': -74.0060}
}
API_URL = 'https://api.openweathermap.org/data/2.5/forecast'
DATA_FILE = 'weather_data.csv'

def initialize_csv():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['City', 'Timestamp', 'Current Temperature', 'Temperature in 3 Hours'])

def fetch_weather():
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        for city, info in CITIES.items():
            response = requests.get(API_URL, params={
                'lat': info['lat'],
                'lon': info['lon'],
                'units': 'metric',
                'appid': API_KEY
            })
            if response.status_code == 200:
                data = response.json()
                current_temperature = data['list'][0]['main']['temp']
                temperature_in_3_hours = data['list'][1]['main']['temp']
                writer.writerow([city, datetime.now().isoformat(), current_temperature, temperature_in_3_hours])
            else:
                print(f"Error fetching data for {city}: {response.status_code}")
                writer.writerow([city, datetime.now().isoformat(), 'N/A', 'N/A'])

if __name__ == "__main__":
    initialize_csv()
    fetch_weather()
