import requests
from pprint import pprint

API_Key = '06934d37176ab9c2660cfe877486ce51'

city = input('Enter city: ')

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)

