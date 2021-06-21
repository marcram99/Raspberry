import board
import digitalio
import busio
import adafruit_si7021
import adafruit_tsl2591

i2c = busio.I2C(board.SCL, board.SDA)
sensor01 = adafruit_si7021.SI7021(i2c)
sensor02 = adafruit_tsl2591.TSL2591(i2c)
seuil_nuit = 40

def read_capt01():
    temp = sensor01.temperature
    hum = sensor01.relative_humidity
    return {'température': temp, 'humidité': hum}

def read_temp():
    return sensor01.temperature

def read_hum():
    return sensor01.relative_humidity

def read_capt02():
    lux = sensor02.lux
    ir = sensor02.infrared
    return {'lux': lux, 'ir':ir}

def read_lum():
    if sensor02.lux > seuil_nuit:
        return "light"
    else:
        return "dark"

 __name__ == '__main__':
    print(capt01())
    print(capt02())
