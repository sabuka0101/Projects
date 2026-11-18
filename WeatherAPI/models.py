class CityNotFoundError(Exception):
    """Raised when the API can't find the city."""


class WeatherReport:
    """Weather for one city."""

    def __init__(self, city, temperature, wind_speed):
        self.__city = city
        self.__temperature = temperature
        self.__wind_speed = wind_speed

    @property
    def city(self):
        return self.__city

    @property
    def temperature(self):
        return self.__temperature

    @property
    def wind_speed(self):
        return self.__wind_speed

    def to_dict(self):
        return {
            "city": self.city,
            "temperature": self.temperature,
            "wind_speed": self.wind_speed,
        }

    def __str__(self):
        return f"{self.city}: {self.temperature}°C, wind {self.wind_speed} km/h"
