#! /usr/bin/python3.5
# encoding:utf-8
import board
import busio
import adafruit_si7021
from pathlib import Path
from datetime import datetime
from config import Config

time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'

logfile = Config.temp_logfile 

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)
temp = sensor.temperature
hum = sensor.relative_humidity

data = f'{time_stamp}_T:{temp:.2f}_H:{hum:.1f}\n'
with open(logfile,'a') as f:
    f.write(data)

