import asyncio
from functools import wraps

import aiohttp

from models import CityNotFoundError, WeatherReport

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def retry(func):
    """Tries the request again (up to 3 times) if the network fails."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        for attempt in range(3):
            try:
                return await func(*args, **kwargs)
            except aiohttp.ClientError:
                if attempt == 2:
                    raise

    return wrapper


@retry
async def get_weather(session, city):
    """Finds the city's coordinates, then gets its weather."""
    async with session.get(GEO_URL, params={"name": city, "count": 1}) as response:
        geo = await response.json()

    if "results" not in geo:
        raise CityNotFoundError(f"City '{city}' not found")

    place = geo["results"][0]
    params = {
        "latitude": place["latitude"],
        "longitude": place["longitude"],
        "current": "temperature_2m,wind_speed_10m",
    }
    async with session.get(WEATHER_URL, params=params) as response:
        data = await response.json()

    current = data["current"]
    return WeatherReport(
        place["name"], current["temperature_2m"], current["wind_speed_10m"]
    )


async def get_many(cities):
    """Gets the weather for all cities at the same time."""
    async with aiohttp.ClientSession() as session:
        tasks = [get_weather(session, city) for city in cities]
        return await asyncio.gather(*tasks, return_exceptions=True)
