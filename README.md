# Weather CLI App

A command line app that give you real time weather data for any city using the OpenWeatherMap API.

## What it does
Type in any city name and get back the current temperature, feels like temperature, humidity, wind speed, and weather description instantly.

## Technologies used
- Python
- Requests
- python-dotenv
- OpenWeatherMap API

## Setup

Clone the repo:
```bash
git clone https://github.com/y6367/web-scraper.git
cd weather-cli
```

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a '.env' file in the root of the project and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_key_here
```

## How to run it
```bash
python3 scraper.py
```

## Example output
```
Enter a city: Seattle

Seattle, WA
Temperature: 72°F
Feels like: 70°F
Humidity: 45%
Wind: 5.2 mph
Clear sky
```