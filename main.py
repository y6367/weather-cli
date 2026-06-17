import datetime
from weather import get_weather
from database import insert_weather

date = datetime.datetime.now().date()
name, temp, feels_like, humidity, wind, description = get_weather("Seattle")
insert_weather(date, name, temp, feels_like, humidity, wind, description)