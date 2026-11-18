import json


class Storage:
    """Saves the city list and weather history to a JSON file."""

    def __init__(self, path="WeatherAPI/data.json"):
        self.__path = path

    def load(self):
        try:
            with open(self.__path, encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"cities": [], "history": []}

    def save(self, data):
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
