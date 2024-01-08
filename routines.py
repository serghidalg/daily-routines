import variables
import pyowm
from gotify import Gotify

def routine_gotify(title,description):
    gotify = Gotify(variables.gotify_url, variables.gotify_key)
    gotify.create_message(description,title=title)

def routine_weather():
    # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    owm = pyowm.OWM(variables.weather_api_key)

    # Replace 'City,Country' with the desired location
    location = 'Madrid'

    observation = owm.weather_manager().weather_at_place(location)
    weather = observation.weather
    if 'rain' in weather.detailed_status.lower():
        description = f"It's raining in {location}!"
    else:
        description = f"No rain in {location} at the moment."
    routine_gotify("Weather update :D",description)

routine_weather()
