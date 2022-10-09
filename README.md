# OpenWeatherMap to InfluxDB

## Description

Fetch weather data from OpenWeatherMap and save it to InfluxDB.

## Table of Contents

* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Author](#author)

## Installation

**Requirements**
- Python 3.10.4
- [requests 2.26.2](https://pypi.org/project/requests/)
- [python-dotenv 0.21.0](https://pypi.org/project/python-dotenv/)
- [influxdb-client 1.32.0](https://pypi.org/project/influxdb-client/)

Clone this repo and run the following from the root folder:
```bash
pip install -r requirements.txt
mv openweathermap.env.example openweathermap.env
mv influxdb.env.example influxdb.env
```

Adjust `openweathermap.env` (see [OpenWeatherMap API Parameters](https://openweathermap.org/current#geo)).

Adjust `influxdb.env`.

## Usage

Test OpenWeatherMap:
```bash
python test_openweathermap.py
```

Current weather:
```bash
python current.py
```

Forecast:
```bash
python forecast.py
```

## Author

- Jonathan Tschanter [GitLab](https://gitlab.com/jmtw) [LinkedIn](https://de.linkedin.com/in/jonathan-tschanter)
