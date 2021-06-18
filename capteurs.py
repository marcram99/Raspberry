import board
import digitalio
import busio
import adafruit_si7021
import adafruit_tsl2591
from pathlib import Path
from datetime import datetime

i2c = busio.I2C(board.SCL, board.SDA)
sensor01 = adafruit_si7021.SI7021(i2c)
sensor02 = adafruit_tsl2591.TSL2591(i2c)

temp = sensor01.temperature
hum = sensor01.relative_humidity
lux = sensor02.lux
ir = sensor02.infrared

def capt01():
    temp = sensor01.temperature
    hum = sensor01.relative_humidity
    results = {'température':temp,
               'humidité':hum
              }
    return results
def capt02():
    lux = sensor02.lux
    ir = sensor02.infrared
    results = {'lux':lux,
               'ir':ir
              }
    return results


if __name__ == '__main__':
    print(capt01())
    print(capt02())
