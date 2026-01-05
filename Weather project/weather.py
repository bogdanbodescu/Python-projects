import os
import requests

api_key = os.getenv("OPENWEATHER_API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str, api_key: str, units: str = "metric") -> dict:
    params = {
        "q": city,
        "appid": api_key,
        "units": units,
        "lang": "ro",
    }
    r = requests.get(API_URL, params=params, timeout=10)

    # OpenWeatherMap returnează JSON și la erori
    data = r.json()

    if r.status_code == 401:
        raise ValueError("Cheie API invalidă (401). Verifică API_KEY.")
    if r.status_code == 404:
        raise ValueError(f"Oraș negăsit: {city}")
    if r.status_code != 200:
        msg = data.get("message", "Eroare necunoscută")
        raise RuntimeError(f"Eroare API ({r.status_code}): {msg}")

    return data


def format_weather(data: dict, units: str) -> str:
    name = data["name"]
    country = data["sys"]["country"]
    desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"].get("speed", 0)

    unit_symbol = "°C" if units == "metric" else "°F" if units == "imperial" else "K"
    wind_unit = "m/s" if units != "imperial" else "mph"

    return (
        f"📍 {name}, {country}\n"
        f"🌤️  {desc}\n"
        f"🌡️  Temp: {temp}{unit_symbol} (feels like {feels}{unit_symbol})\n"
        f"💧 Umiditate: {humidity}%\n"
        f"💨 Vânt: {wind} {wind_unit}"
    )


def main():

    if not api_key:
        print("Lipsește cheia API. Setează variabila de mediu OPENWEATHER_API_KEY.")
        print("Exemplu (CMD): setx OPENWEATHER_API_KEY \"CHEIA_TA\"")
        return

    units_choice = input("Unități (C/F) [C]: ").strip().upper()
    units = "imperial" if units_choice == "F" else "metric"

    while True:
        city = input("\nIntrodu orașul (sau ENTER ca să ieși): ").strip()
        if not city:
            print("Bye 👋")
            break

        try:
            data = get_weather(city, api_key, units=units)
            print("\n" + format_weather(data, units))
        except Exception as e:
            print(f"❌ {e}")


if __name__ == "__main__":
    main()