import asyncio

from api import get_many
from models import WeatherReport
from storage import Storage


def show_weather(cities, data):
    """Gets the weather for the cities, prints it and adds it to the history."""
    results = asyncio.run(get_many(cities))
    for result in results:
        if isinstance(result, WeatherReport):
            print(result)
            data["history"].append(result.to_dict())
        else:
            print(f"Error: {result}")


storage = Storage()
data = storage.load()

while True:
    print("\n1. Weather for a city")
    print("2. Weather for all my cities")
    print("3. Add city")
    print("4. Remove city")
    print("5. Show history")
    print("6. Exit")
    choice = input("Choose: ")

    if choice == "1":
        city = input("City: ").strip()
        if city:
            show_weather([city], data)
        else:
            print("Error: City can't be empty")

    elif choice == "2":
        if data["cities"]:
            show_weather(data["cities"], data)
        else:
            print("No cities yet.")

    elif choice == "3":
        city = input("City to add: ").strip()
        if not city:
            print("Error: City can't be empty")
        elif city in data["cities"]:
            print("Already in the list.")
        else:
            data["cities"].append(city)
            print(f"Added {city}")

    elif choice == "4":
        city = input("City to remove: ").strip()
        if city in data["cities"]:
            data["cities"].remove(city)
            print(f"Removed {city}")
        else:
            print("Not in the list.")

    elif choice == "5":
        for record in data["history"]:
            print(
                f"{record['city']}: {record['temperature']}°C, wind {record['wind_speed']} km/h"
            )
        if not data["history"]:
            print("No history yet.")

    elif choice == "6":
        storage.save(data)
        print("Saved. Goodbye!")
        break

    else:
        print("Choose 1-6.")

    storage.save(data)
