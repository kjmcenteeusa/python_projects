#WeatherReport.py

# Kevin McEntee
# 4/1/2024
# Send Weather forecast via messaging service.

# Notes
# Must install requests, plyer, discord.py
# Command Prompt: pip install requests
# Command Prompt: pip install plyer
# Command Prompt: pip install discord.py

# import required modules
import requests
import json

weatherAPI = '75a77152b4364c4b56380f7e4fcfe4c7'
weatherLocation = "bohemia,ny,us"
weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={weatherLocation}&units=imperial&APPID={weatherAPI}")
weatherCurrent = weatherData.json()['weather'][0]['main']
weatherCurrTemp = str(round(weatherData.json()['main']['temp']))
weatherTempTempMin = str(round(weatherData.json()['main']['temp_min']))
weatherDescription = weatherData.json()['weather'][0]['description']
weatherClouds = weatherData.json()['clouds']['all']

print(weatherCurrent)
print(weatherCurrTemp)
print(weatherTempTempMin)
print(weatherDescription)
print(weatherClouds)

