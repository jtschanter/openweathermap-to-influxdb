#!/usr/bin/env python3

from dotenv import dotenv_values
import json
import requests

class OpenWeatherMap:

    def __init__(self):
        config = dotenv_values("openweathermap.env")
        self.lat = config["LAT"]
        self.lon = config["LON"]
        self.appid = config["APPID"]
        self.cnt = config["CNT"]
        self.units = config["UNITS"]
        self.lang = config["LANG"]

    def get_forecast(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={self.appid}&cnt={self.cnt}&units={self.units}&lang={self.lang}")
        return response.json()

    def get_current(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.appid}&units={self.units}&lang={self.lang}")
        return response.json()
