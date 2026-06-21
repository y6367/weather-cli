# Weather CLI App

A command line app that gives you real time weather data for any city using the OpenWeatherMap API, with daily logging to a local database.

> **Note:** `test-scraper.py` was used strictly for learning and experimenting during development. It is unrelated to the weather app. The main application is in `weather.py`, `database.py`, and `main.py`.

## What it does

Type in any city name and get back the current temperature, feels like temperature, humidity, wind speed, and weather description instantly. The app also logs daily weather data to a local SQLite database, allowing you to track trends over time.

## Technologies used

- Python
- Requests
- python-dotenv
- SQLite3
- OpenWeatherMap API

## Project structure

- `weather.py` — handles API calls to OpenWeatherMap (can be run standalone for a single city lookup)
- `database.py` — handles all SQLite database operations (creating tables, inserting records)
- `main.py` — connects weather and database logic together; intended for automated daily runs
- `test-scraper.py` — used for learning, unrelated to the app

## Setup

Clone the repo:
```bash
git clone https://github.com/joew63/weather-cli.git
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

Create a `.env` file in the root of the project and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_key_here
```

## How to run it

**Standalone lookup** (asks for a city, prints current weather):
```bash
python3 weather.py
```

**Logging run** (used for automated daily tracking, no input required):
```bash
python3 main.py
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

## Automation

This project is set up to run daily via a cron job, automatically logging weather data to `data.db` without manual input. To replicate this, set up a cron job pointing to `main.py` using absolute paths to your Python interpreter and script, for example:
```
0 8 * * * /full/path/to/venv/bin/python3 /full/path/to/main.py
```

## Database

Weather data is stored locally in `data.db` (excluded from version control). The database is created automatically the first time the app runs.
