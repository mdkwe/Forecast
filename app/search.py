from datetime import datetime
import requests
import math

from config import API_KEY_WEATHER, API_KEY_GEO


import requests
from requests.structures import CaseInsensitiveDict

# def autocomplete(city): 
#       API_URL = ('https://api.geoapify.com/v1/geocode/autocomplete?text={}&limit=5&type=city&format=json&apiKey={}')
#       try:
#             # print(API_URL.format(city, API_KEY_GEO))
#             data = requests.get(API_URL.format(city, API_KEY_GEO)).json() 

#             # print(data)

#       except Exception as exc:
#             print(exc)
#             data = None
#       return data

# dic = {"city" : [], "lon" : [], "lat" : []}
# for i in range(1, len(data['results'])) : 
#       dic['city'] = data['results'][i]['formatted']
#       dic['lon'] = data['results'][i]['lon']
#       dic['lat'] = data['results'][i]['lat'] 

# dic

# def query_api(city):
#       API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
#       try:
#             print(API_URL.format(city, API_KEY_WEATHER))
#             data = requests.get(API_URL.format(city, API_KEY_WEATHER)).json()
#       except Exception as exc:
#             print(exc)
#             data = None
#       return data

# data = query_api(city="Londres")
