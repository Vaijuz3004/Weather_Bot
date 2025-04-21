import requests
import os 
from conf import apis
from exception import CustomException
from logger import logging
weather_api_key = apis["WEATHER_API_KEY"]

def get_weather(city):
    city = city.split(" ")
    city = city[-1]
    city = city.strip()
    print(f"City: {city}")
    if city.lower() == "unknown":
        return "I could not understand the city name... Please try again"
    base_url = f"http://api.weatherapi.com/v1/current.json"
    params = {
        "key": weather_api_key,
        "q": city,
        "aqi": "no"
            }
    try:
        response = requests.get(base_url, params = params)
        if response.status_code == 200:
            data = response.json()
            location = data["location"]["name"]
            region = data["location"]["region"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            icon = data["current"]["condition"]["icon"]
            condition_lower = condition.lower()
            emoji = "☀️" if "sun" in condition_lower else \
                        "🌧️" if "rain" in condition_lower else \
                        "⛅" if "cloud" in condition_lower else \
                        "❄️" if "snow" in condition_lower else "🌈"
            return f"{emoji} {location}, {region}, {country}. Its {temp_c}°C right now."
        else:
            logging.error(f"Error fetching weather data: {response.status_code}")
            return f"I could not fetch the weather data for {city} ... Please try again"
    except CustomException as e:
        logging.error(f"Error in get_weather: {e}")
        print(f"Error in get_weather: {e}")
        return "I could not fetch the weather data... Please try again"

# if __name__ == "__main__":
#     city = "Pune"
#     print(get_weather(city))