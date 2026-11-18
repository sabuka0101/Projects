# Asynchronous Weather Dashboard

A console app that shows the current weather for cities, using the free
[Open-Meteo](https://open-meteo.com) API (no API key needed).

## Features

- Get the weather for any city by name
- Get the weather for all saved cities at the same time (async)
- Add and remove cities from your list
- Weather history saved to `data.json`

## Project structure

| File         | Purpose                                |
| ------------ | -------------------------------------- |
| `main.py`    | the menu, run this file                |
| `api.py`     | async requests to the Open-Meteo API   |
| `models.py`  | `WeatherReport` class and custom error |
| `storage.py` | saving and loading `data.json`         |

## How to run

Run these from the main folder of this repository (the one that contains
`WeatherAPI`), not from inside `WeatherAPI`:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r WeatherAPI/requirements.txt
python WeatherAPI/main.py
```

## Example

```
1. Weather for a city
2. Weather for all my cities
3. Add city
4. Remove city
5. Show history
6. Exit
Choose: 1
City: Tbilisi
Tbilisi: 20.1°C, wind 25.3 km/h
```
