from microbit import *
from microbit import i2c
from oled import initialize, clear_oled, add_text
import neopixel
from motor_driver import servomotor, dcmotor
from TempAndHum import TempAndHumInit, ReadTemperature, ReadHumidity
from TouchSensor import touchinit, play_piano, piano_touched

#Pin Defines
LDR_pin = pin0
Pot_pin = pin1
Button_pin = pin2
Motion_pin = pin13
RGB_pin = pin8
Relay_pin = pin16
num_leds = 3

#Init functions
initialize()
TempAndHumInit()
touchinit()

#Neopixel
np = neopixel.NeoPixel(RGB_pin, num_leds)

#MotorDriver
#angle must be between 0 and 90
servomotor(2,90)
#speed must be between 0 and 255
#direction must be 0 or 1. 0 is forward, 1 is backward
dcmotor(1,255,1)

#Relay
Relay_pin.write_digital(1)
sleep(2000)
Relay_pin.write_digital(0)

clear_oled()

while True:
    display.show(Image.HEART)

    #Touch Sensor
    #play_piano()
    #touch = piano_touched("C2") #String
    #print(touch)
    
    #Temperature
    temp = ReadTemperature()
    #print("Temperature: {:.2f}°C".format(temp))

    #Humidity
    hum = ReadHumidity()
    #print("Humidity: {:.2f}%".format(hum))
    
    #Oled
    add_text(0, 0, "PicoBricks")
    add_text(0, 1, "Temp :")
    add_text(6,1,str(float(temp)))
    add_text(0, 2, "Hum :")
    add_text(6,2,str(float(hum)))
    sleep(500)
    
    #Neopixel
    np[0] = (0, 0, 255)
    np[1] = (0, 255, 0)
    np[2] = (255, 0, 0)
    np.show()
    
    #LDR
    read_ldr = LDR_pin.read_analog()
    #print(read_ldr)
    
    #Pot
    read_pot = Pot_pin.read_analog()
    #print(read_pot)
    
    #Button
    read_button = Button_pin.read_digital()
    #print(read_button)

    #Motion Sensor
    read_motion = Motion_pin.read_digital()
    #print(read_motion)
