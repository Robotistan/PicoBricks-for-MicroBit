from microbit import *
from microbit import i2c

shtc_address = 0x70

def TempAndHumInit():
    i2c.write(shtc_address, bytes([0x80, 0x5D]))
    sleep(100)
    i2c.write(shtc_address, bytes([0x35, 0x17]))

def ReadTemperature():
    i2c.write(shtc_address, bytes([0x78, 0x66]))
    sleep(13)
    data = i2c.read(shtc_address, 2)
    sleep(1)
    temperature = ((data[0] << 8) | data[1]) * 175 / 65535 - 45

    return temperature

def ReadHumidity():
    i2c.write(shtc_address, bytes([0x78, 0x66]))
    sleep(13)
    data = i2c.read(shtc_address, 5)
    sleep(1)
    humidity = ((data[3] << 8) | data[4]) * 100 / 65535

    return humidity
        
   
