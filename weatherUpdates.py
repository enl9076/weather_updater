import pandas as pd
import requests
import json
import datetime
import os
from plyer import notification
from dotenv import load_dotenv
load_dotenv()

LATITUDE=os.getenv('LATITUDE')
LONGITUDE=os.getenv('LONGITUDE')
APIkey=os.getenv('API_key')

## Query the API
url = f'https://weather.googleapis.com/v1/currentConditions:lookup?key={APIkey}&location.latitude={LATITUDE}&location.longitude={LONGITUDE}&unitsSystem=IMPERIAL'
response = requests.request("GET", url)
weather_dict = json.loads(response.text)


## Determine if there are any weather alerts
def get_alerts():
    if 'alerts' not in weather_dict.keys():
        alerts = "No weather alerts"
        return alerts
    else:
        alerts = []
        for i in weather_dict['alerts']:
            alerts.append(i['event'])
        for i in alerts:
            return i

## Get current weather condition info from the JSON data
current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
desc = weather_dict['weatherCondition']['description']['text']
temp = weather_dict['temperature']['degrees']
feels_like = weather_dict['feelsLikeTemperature']['degrees']
storm_prob = weather_dict['thunderstormProbability']
alerts = get_alerts()

## Set up notification
notification.notify(title = "Weather Update",
                    message = f"Now: {current_time} \nIt is currently {temp}°F but feels like {feels_like}\nIt is {desc} with {storm_prob}% chance of storms.\n{alerts}", 
                    timeout=15)