#! /usr/bin/python3.5
# encoding:utf-8
import capteurs2 as capteurs
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
with open(debug_logfile, 'a') as f:
    f.write(f"{time_stamp} templogger en cours\n")

temp = capteurs.read_temp()
hum = capteurs.read_hum()
data = f'{time_stamp}_T:{temp:.2f}_H:{hum:.1f}\n'
with open(logfile,'a') as f:
    f.write(data)

