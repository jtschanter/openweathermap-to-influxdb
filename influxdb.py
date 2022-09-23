#!/usr/bin/env python3

from dotenv import dotenv_values
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDB:

    def __init__(self):
        config = dotenv_values("influxdb.env")
        self.url = config["URL"]
        self.token = config["TOKEN"]
        self.org = config["ORG"]
        self.bucket = config["BUCKET"]

    def write(self, sequence):
        with InfluxDBClient(url=self.url, token=self.token, org=self.org) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            write_api.write(self.bucket, self.org, sequence, write_precision=WritePrecision.S)

def get_sequence(measurement, tags, field_value_pairs, timestamp=None):
    sequence = f"{measurement}"
    for i in range(len(tags)):
        tag = tags[i]
        sequence += f",{tag}"
    for i in range(len(field_value_pairs)):
        field_value_pair = field_value_pairs[i]
        if i == 0:
            sequence += f" {field_value_pair}"
        else:
            sequence += f",{field_value_pair}"
    if timestamp:
        sequence += f" {timestamp}"
    return sequence
