#!/usr/bin/env python3

from openweathermap import OpenWeatherMap

owm = OpenWeatherMap()

current = owm.get_current()
print(current)

forecast = owm.get_forecast()
print(forecast)
