import board
import digitalio
import busio
import adafruit_si7021
import adafruit_tsl2591
from config import Config
from datetime import datetime

debug_logfile = Config.debug_logfile
if not debug_logfile.exists():
    debug_logfile.touch()

i2c = busio.I2C(board.SCL, board.SDA)
badcaptor = 1
connter = 0
while badcaptor:
    try:
        sensor01 = adafruit_si7021.SI7021(i2c)
        badcaptor = 0
    except RuntimeError:
        badcaptor = 1
        counter += 1
    else:
        with open(debug_logfile, 'a') as f:
            f.write(f'{datetime.now()} DEBUG: Capteur init aprés {counter} essais\n')
#

sensor02 = adafruit_tsl2591.TSL2591(i2c)

def read_capt01():
    temp = sensor01.temperature
    hum = sensor01.relative_humidity
    return {'température': temp, 'humidité': hum}

def read_temp():
    return sensor01.temperature

def read_hum():
    return sensor01.relative_humidity

def read_ir():
    return sensor02.infrared

def read_lux():
    return sensor02.lux

def read_capt02():
    lux = sensor02.lux
    ir = sensor02.infrared
    return {'lux': lux, 'ir':ir}

def read_lum(seuil_nuit):
    """Renvoi la valeur 'light' ou 'dark' en fonction du param:'seuil nuit'""" 
    if sensor02.lux > seuil_nuit:
        return "light"
    else:
        return "dark"

if __name__ == '__main__':
     print(read_capt01())
     print(read_capt02())
