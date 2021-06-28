import board
import digitalio
import busio
import adafruit_si7021
import adafruit_tsl2591
from datetime import datetime
from config import Config 

logfile = Config.debug_logfile
if not logfile.exists():
    logfile.touch()
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor01 = adafruit_si7021.SI7021(i2c)
    sensor02 = adafruit_tsl2591.TSL2591(i2c)
except Error as erreur:
    with open(logfile,'a') as f:
        f.write(f'{datetime.now()}_ERROR_from capteurs.py:{erreur}')

def read_capt01():
    try:
        temp = sensor01.temperature
        hum = sensor01.relative_humidity
        return {'température': temp, 'humidité': hum}
    except Error as erreur:    
        with open(logfile,'a') as f:
            f.write(f'{datetime.now()}_ERROR_from capteurs.readcapt01:{erreur}')
            return {'température': 0, 'humidité': 0}
        
def read_temp():
    try:
        return sensor01.temperature
    except Error as erreur:    
        with open(logfile,'a') as f:
            f.write(f'{datetime.now()}_ERROR_from capteurs.read_temp:{erreur}')
            return 0

def read_hum():
    try:
        return sensor01.trelative_humidity
    except Error as erreur:    
        with open(logfile,'a') as f:
            f.write(f'{datetime.now()}_ERROR_from capteurs.read_hum:{erreur}')
            return 0

def read_capt02():
    try:
        lux = sensor02.lux
        ir = sensor02.infrared
        return {'lux': lux, 'ir':ir}
    except Error as erreur:
        with open(logfile,'a') as f:
            f.write(f'{datetime.now()}_ERROR_from capteurs.read_capt02:{erreur}')
            return {'lux': 0, 'ir': 0}

def read_lum(seuil_nuit):
    try:
        if sensor02.lux > seuil_nuit:
            return "light"
        else:
            return "dark"
    except Error as erreur:
        f.write(f'{datetime.now()}_ERROR_from capteurs.read_lum:{erreur}')
        return 'dark'

 __name__ == '__main__':
    print(capt01())
    print(capt02())
