import os, json, requests, time
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

city = input("enter a city: ")
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
response = requests.get(url)
data = response.json()

name = data[0]["name"]
lat = data[0]["lat"]
lon = data[0]["lon"]

# print(response.text)
# print(name)
# print(lat)
# print(lon)

weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}"
weather_request = requests.get(weather)
weather_data = weather_request.json()

temp = weather_data["main"]["temp"]
description = weather_data["weather"][0]["description"]

print(f"The temperature in {name} is {temp} degrees fahrenheit, it currently has {description}")