#! /usr/bin/python3.5
# encoding:utf-8
import capteurs
from pathlib import Path
from datetime import datetime
from config import Config

time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'
logfile = Config.temp_logfile
temp = capteurs.read_temp()
hum = capteurs.read_hum()
data = f'{time_stamp}_T:{temp:.2f}_H:{hum:.1f}\n'
with open(logfile,'a') as f:
    f.write(data)
