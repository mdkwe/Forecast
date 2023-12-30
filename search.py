from datetime import datetime
import requests
import math
import pytz
import os

# import API KEYS
API_KEY_WEATHER = os.getenv("API_KEY_WEATHER")


def query_api(location, unit = 'metric'):
      API_URL =('https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=minutely,alerts&mode=json&units={}&&appid={}')
      try:
            # print(API_URL.format(location["lat"], location["lon"], unit, API_KEY_WEATHER))
            data = requests.get(API_URL.format(location["lat"], location["lon"],unit, API_KEY_WEATHER)).json()
      except Exception as exc:
            print(exc)
            data = None
      return data

import pytz
from datetime import datetime

def format_datetime(unix_timestamp, timezone, type='date'):
    """Convert a Unix timestamp to a formatted date or time in a specified timezone."""
    tz = pytz.timezone(timezone)
    dt = datetime.fromtimestamp(unix_timestamp, tz)

    if type == "date":
        return dt.strftime('%a %d/%m')
    elif type == 'hour':
        return dt.strftime('%H:%M:%S')
    else:
        # Default or fallback format, can be adjusted as needed
        return dt.strftime('%Y-%m-%d %H:%M:%S')

def convert_mps_to_kph(speed_mps):
    speed_kph = speed_mps * 3.6
    return round(speed_kph,1)

