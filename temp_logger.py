#! /usr/bin/python3.5
# encoding:utf-8
import board
import busio
import adafruit_si7021
from pathlib import Path
from datetime import datetime

time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'
date_stamp = f'{datetime.now():%Y-%m-%d}'

logfiles_path = Path.home().joinpath('Marc-perso/Code/logfiles')
if not logfiles_path.exists():
    Path.mkdir(logfiles_path)
logfile_name = f'{date_stamp}_capt01.log'    
logfile = logfiles_path.joinpath(logfile_name)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)
temp = sensor.temperature
hum = sensor.relative_humidity

data = f'{time_stamp}_T:{temp:.2f}_H:{hum:.1f}\n'
with open(logfile,'a') as f:
    f.write(data)
