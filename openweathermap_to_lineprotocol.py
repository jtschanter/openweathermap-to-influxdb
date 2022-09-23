#!/usr/bin/env python3

from influxdb import get_sequence

class OpenWeatherMapToLineProtocol:

    def __init__(self, timestamp, forecast=0):
        self.tags = [f"forecast={forecast:03d}h"]
        self.timestamp = timestamp

    def __get_sequence(self, measurement, field_value_pairs):
        return get_sequence(
            measurement=measurement,
            tags=self.tags,
            field_value_pairs=field_value_pairs,
            timestamp=self.timestamp
        )

    def convert_sun(self, sunrise, sunset):
        return self.__get_sequence(
            measurement="sun",
            field_value_pairs=[
                f"sunrise={sunrise}",
                f"sunset={sunset}"
            ]
        )

    def convert_temperatur(self, temp, min, max, feels_like):
        return self.__get_sequence(
            measurement="temperature",
            field_value_pairs=[
                f"temp={temp}",
                f"min={min}",
                f"max={max}",
                f"feels_like={feels_like}"
            ]
        )

    def convert_atmospheric_pressure(self, pressure, sea_level, grnd_level):
        return self.__get_sequence(
            measurement="pressure",
            field_value_pairs=[
                f"pressure={pressure}",
                f"sea_level={sea_level}",
                f"grnd_level={grnd_level}"
            ]
        )

    def convert_humidity(self, humidity):
        return self.__get_sequence(
            measurement="humidity",
            field_value_pairs=[
                f"humidity={humidity}"
            ]
        )

    def convert_weather(self, id, main, description):
        return self.__get_sequence(
            measurement="weather",
            field_value_pairs=[
                f"id={id}",
                f"main=\"{main}\"",
                f"description=\"{description}\""
            ]
        )

    def convert_visibility(self, visibility):
        return self.__get_sequence(
            measurement="visibility",
            field_value_pairs=[
                f"visibility={visibility}"
            ]
        )

    def convert_wind(self, speed, deg, gust):
        return self.__get_sequence(
            measurement="wind",
            field_value_pairs=[
                f"speed={speed}",
                f"deg={deg}",
                f"gust={gust}"
            ]
        )

    def convert_clouds(self, clouds):
        return self.__get_sequence(
            measurement="clouds",
            field_value_pairs=[
                f"clouds={clouds}"
            ]
        )

    def convert_rain(self, rain_1=None, rain_3=None):
        field_value_pairs = []
        if rain_1:
            field_value_pairs.append(f"1h={rain_1}")
        if rain_3:
            field_value_pairs.append(f"3h={rain_3}")
        return self.__get_sequence(
            measurement="rain",
            field_value_pairs=field_value_pairs
        )

    def convert_snow(self, snow_1=None, snow_3=None):
        field_value_pairs = []
        if snow_1:
            field_value_pairs.append(f"1h={snow_1}")
        if snow_3:
            field_value_pairs.append(f"3h={snow_3}")
        return self.__get_sequence(
            measurement="snow",
            field_value_pairs=field_value_pairs
        )

    def convert_pop(self, pop):
        return self.__get_sequence(
            measurement="pop",
            field_value_pairs=[
                f"pop={pop}"
            ]
        )
