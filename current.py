#!/usr/bin/env python3

from openweathermap import OpenWeatherMap
from influxdb import InfluxDB
from openweathermap_to_lineprotocol import OpenWeatherMapToLineProtocol

influxdb = InfluxDB()
sequences = []

owm = OpenWeatherMap()
current = owm.get_current()

if current["cod"] == 200:

    timestamp = current["dt"] # uct
    converter = OpenWeatherMapToLineProtocol(timestamp)

    # sunrise / sunset
    sunrise = current["sys"]["sunrise"]
    sunset = current["sys"]["sunset"]
    sequence = converter.convert_sun(sunrise, sunset)
    sequences.append(sequence)

    # temperature
    temp = current["main"]["temp"]
    min = current["main"]["temp_min"]
    max = current["main"]["temp_max"]
    feels_like = current["main"]["feels_like"]
    sequence = converter.convert_temperatur(temp, min, max, feels_like)
    sequences.append(sequence)

    # atmospheric pressure
    pressure = current["main"]["pressure"]
    sea_level = current["main"]["sea_level"]
    grnd_level = current["main"]["grnd_level"]
    sequence = converter.convert_atmospheric_pressure(pressure, sea_level, grnd_level)
    sequences.append(sequence)

    # humidity
    humidity = current["main"]["humidity"]
    sequence = converter.convert_humidity(humidity)
    sequences.append(sequence)

    # weather (list)
    weather = current["weather"][0]
    id = weather["id"]
    main = weather["main"]
    description = weather["description"].replace(" ", "-")
    sequence = converter.convert_weather(id, main, description)
    sequences.append(sequence)

    # visibility
    visibility = current["visibility"]
    sequence = converter.convert_visibility(visibility)
    sequences.append(sequence)

    # wind
    speed = current["wind"]["speed"]
    deg = current["wind"]["deg"]
    gust = current["wind"]["gust"]
    sequence = converter.convert_wind(speed, deg, gust)
    sequences.append(sequence)

    # clouds
    clouds = current["clouds"]["all"]
    sequence = converter.convert_clouds(clouds)
    sequences.append(sequence)

    # rain
    if "rain" in current:
        rain_1 = current["rain"]["1h"]
        rain_3 = current["rain"]["3h"]
        sequence = converter.convert_rain(rain_1=rain_1, rain_3=rain_3)
        sequences.append(sequence)

    # snow
    if "snow" in current:
        snow_1 = current["snow"]["1h"]
        snow_3 = current["snow"]["3h"]
        sequence = converter.convert_rain(snow_1=snow_1, snow_3=snow_3)
        sequences.append(sequence)

    influxdb.write(sequences)
