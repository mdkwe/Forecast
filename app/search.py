from datetime import datetime
import requests
import math
import pytz

from config import API_KEY_WEATHER, API_KEY_GEO


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






# import requests
# from requests.structures import CaseInsensitiveDict

# def geocode(city): 
#       API_URL = ('https://api.geoapify.com/v1/geocode/autocomplete?text={}&limit=5&type=city&format=json&apiKey={}')
#       try:
#             # print(API_URL.format(city, API_KEY_GEO))
#             data = requests.get(API_URL.format(city, API_KEY_GEO)).json()
#       except Exception as exc:
#             print(exc)
#             data = None
#       return data

# dic = {"city" : [], "lon" : [], "lat" : []}
# for i in range(1, len(data['results'])) : 
#       dic['city'] = data['results'][i]['formatted']
#       dic['lon'] = data['results'][i]['lon']
#       dic['lat'] = data['results'][i]['lat'] 

# def geocode(city):
#       API_URL =('http://api.openweathermap.org/geo/1.0/direct?q={}&mode=json&units=metric&limit=1&appid={}')
#       location = {}
#       try:
#             # print(API_URL.format(city, API_KEY_WEATHER))
#             data = requests.get(API_URL.format(city, API_KEY_WEATHER)).json()
#             location['name'] = data[0]['name'], data[0]['state'], data[0]['country']
#             location['lon'] = data[0]['lon']
#             location['lat'] = data[0]['lat'] 
#       except Exception as exc:
#             print(exc)
#             data = None
#       return location
# location = {}
# location["lat"] = 51.509865
# location["lon"] = -0.118092
# data = query_api(location=location)

# temperature = data["current"]["temp"] #temperature
# feels_like = data["current"]["feels_like"]

# current_time = convert_timestamp_to_datetime(data["current"]["dt"], data["timezone"])
# date_time = current_time.strftime("%x")
# time = current_time.strftime("%X")
# hourly_wind = convert_mps_to_kph(data["hourly"][0]["wind_speed"] )
# hourly_pop = data["hourly"][0]["pop"]
# weather_description =  data["current"]["weather"][0]["description"]
# weather_icon =  data["current"]["weather"][0]["icon"] + "@2x.png"