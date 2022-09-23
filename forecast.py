#!/usr/bin/env python3

import time

from openweathermap import OpenWeatherMap
from influxdb import InfluxDB
from openweathermap_to_lineprotocol import OpenWeatherMapToLineProtocol

influxdb = InfluxDB()
sequences = []

owm = OpenWeatherMap()
forecasts = owm.get_forecast()

if forecasts["cod"] == "200":

    timestamp = int(time.time())
    converter = OpenWeatherMapToLineProtocol(timestamp)

    # sunrise / sunset
    sunrise = forecasts["city"]["sunrise"]
    sunset = forecasts["city"]["sunset"]
    sequence = converter.convert_sun(sunrise, sunset)
    sequences.append(sequence)

    for i in range(len(forecasts["list"])):

        forecast = forecasts["list"][i]
        forecast_for = (i + 1) * 3

        forecast_timestamp = forecast["dt"]
        converter = OpenWeatherMapToLineProtocol(timestamp, forecast_for)

        # temperature
        temp = forecast["main"]["temp"]
        min = forecast["main"]["temp_min"]
        max = forecast["main"]["temp_max"]
        feels_like = forecast["main"]["feels_like"]
        sequence = converter.convert_temperatur(temp, min, max, feels_like)
        sequences.append(sequence)

        # atmospheric pressure
        pressure = forecast["main"]["pressure"]
        sea_level = forecast["main"]["sea_level"]
        grnd_level = forecast["main"]["grnd_level"]
        sequence = converter.convert_atmospheric_pressure(pressure, sea_level, grnd_level)
        sequences.append(sequence)

        # humindity
        humidity = forecast["main"]["humidity"]
        sequence = converter.convert_humidity(humidity)
        sequences.append(sequence)

        # weather (list)
        weather = forecast["weather"][0]
        id = weather["id"]
        main = weather["main"]
        description = weather["description"].replace(" ", "-")
        sequence = converter.convert_weather(id, main, description)
        sequences.append(sequence)

        # visibility
        visibility = forecast["visibility"]
        sequence = converter.convert_visibility(visibility)
        sequences.append(sequence)

        # wind
        speed = forecast["wind"]["speed"]
        deg = forecast["wind"]["deg"]
        gust = forecast["wind"]["gust"]
        sequence = converter.convert_wind(speed, deg, gust)
        sequences.append(sequence)

        # clouds
        clouds = forecast["clouds"]["all"]
        sequence = converter.convert_clouds(clouds)
        sequences.append(sequence)

        # probability of precipitation
        pop = forecast["pop"]
        sequence = converter.convert_pop(pop)
        sequences.append(sequence)


        # rain
        if "rain" in forecast:
            rain_3 = forecast["rain"]["3h"]
            sequence = converter.convert_rain(rain_3=rain_3)
            sequences.append(sequence)

        # snow
        if "snow" in forecast:
            snow_3 = forecast["snow"]["3h"]
            sequence = converter.convert_rain(snow_3=snow_3)
            sequences.append(sequence)

    influxdb.write(sequences)
