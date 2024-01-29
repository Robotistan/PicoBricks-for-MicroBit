from microbit import *
from microbit import i2c
from oled import initialize, clear_oled, add_text
import neopixel
from motor_driver import servomotor, dcmotor
from TempAndHum import TempAndHumInit, ReadTemperature, ReadHumidity

#Pin Defines
LDR_pin = pin0
Pot_pin = pin1
Button_pin = pin2
Motion_pin = pin13
RGB_pin = pin8
Relay_pin = pin16
num_leds = 3

#OLED
initialize()

#Neopixel
np = neopixel.NeoPixel(RGB_pin, num_leds)

#Relay
Relay_pin.write_digital(1)
sleep(2000)
Relay_pin.write_digital(0)

#MotorDriver
#angle must be between 0 and 90
servomotor(2,90)
#speed must be between 0 and 255
#direction must be 0 or 1. 0 is forward, 1 is backward
dcmotor(1,255,1)

while True:
    #OLED
    clear_oled()
    add_text(0, 0, "PicoBricks")
    sleep(1000)
    
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
    print(read_button)

    #Motion Sensor
    read_motion = Motion_pin.read_digital()
    print(read_motion)
