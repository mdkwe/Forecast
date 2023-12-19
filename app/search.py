from datetime import datetime
import requests
import math

from config import API_KEY_WEATHER, API_KEY_GEO


# import requests
# from requests.structures import CaseInsensitiveDict

def geocode(city): 
      API_URL = ('https://api.geoapify.com/v1/geocode/autocomplete?text={}&limit=5&type=city&format=json&apiKey={}')
      try:
            # print(API_URL.format(city, API_KEY_GEO))
            data = requests.get(API_URL.format(city, API_KEY_GEO)).json()
      except Exception as exc:
            print(exc)
            data = None
      return data

# dic = {"city" : [], "lon" : [], "lat" : []}
# for i in range(1, len(data['results'])) : 
#       dic['city'] = data['results'][i]['formatted']
#       dic['lon'] = data['results'][i]['lon']
#       dic['lat'] = data['results'][i]['lat'] 

# def geocode(city):
#       API_URL =('http://api.openweathermap.org/geo/1.0/direct?q={}&mode=json&units=metric&limit=5&appid={}')
#       try:
#             # print(API_URL.format(city, API_KEY_WEATHER))
#             data = requests.get(API_URL.format(city, API_KEY_WEATHER)).json()
#       except Exception as exc:
#             print(exc)
#             data = None
#       return data

def query_api(lon, lat):
      API_URL =('https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=minutely,alerts&mode=json&units=metric&appid={}')
      try:
            print(API_URL.format(lat, lon, API_KEY_WEATHER))
            data = requests.get(API_URL.format(lat, lon, API_KEY_WEATHER)).json()
      except Exception as exc:
            print(exc)
            data = None
      return data