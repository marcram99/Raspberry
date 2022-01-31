#! /usr/bin/python3.5
# encoding:utf-8
import capteurs2 as capteurs
import digitalio
import busio
import adafruit_si7021
import adafruit_tsl2591

from pathlib import Path
from datetime import datetime
from config import Config


time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'

debug_logfile = Config.debug_logfile
if not debug_logfile.exists():
    debug_logfile.touch()
logfile = Config.temp_logfile
if not logfile.exists():
    logfile.touch()

i2c = busio.I2C(board.SCL, board.SDA)
badcaptor = 1
counter = 0
while badcaptor:
    try:
        sensor01 = adafruit_si7021.SI7021(i2c)
        badcaptor = 0
    except RuntimeError:
        badcaptor = 1
        counter += 1
    else:
        with open(debug_logfile, 'a') as f:
            f.write(f'{time_stamp} DEBUG: Capteur init aprés {counter} essais\n')

temp = sensor01.temperature
hum = sensor01.relative_humidity 
data = f'{time_stamp}_T:{temp:.2f}_H:{hum:.1f}\n'
with open(logfile,'a') as f:
    f.write(data)

