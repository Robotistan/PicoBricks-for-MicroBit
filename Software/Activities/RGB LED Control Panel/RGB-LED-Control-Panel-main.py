#RGB LED Control Panel Projects
from microbit import *
from picobricks import *
import neopixel

# Pin Initialization
RGB_Pin = pin8
Num_Leds = 3
Pot_Pin = pin1
Button_Pin = pin2

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
np = neopixel.NeoPixel(RGB_Pin, Num_Leds)

#Neopixel
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np.show()

pot_value=0
counter=0
r=0
g=0
b=0

while True:
    oldpot=pot_value
    pot_value = round(round( Pot_Pin.read_analog() - 0 ) * ( 255 - 0 ) / ( 1023 - 0 ) + 0)
    if oldpot!=pot_value:
        oled.add_text(5,3,"    ")
    oled.add_text(5,3,str(int(pot_value)))
    oled.add_text(1,0,"R __ G __ B")
    button = Button_Pin.read_digital()
    if button==1:
        display.show('R')
        o_r= r
        r = pot_value
        if o_r != r:
            oled.add_text(1,2,"    ")
        oled.add_text(1,2,str(int(pot_value)))

    if button_a.is_pressed():
        display.show('G')
        o_g=g
        g=pot_value
        if o_g==g:
            oled.add_text(5,2,"    ")
        oled.add_text(5,2,str(int(pot_value)))
        
    if button_b.is_pressed():
        display.show('B')
        o_b=b
        b=pot_value
        if o_b==b:
            oled.add_text(9,2,"    ")
        oled.add_text(9,2,str(int(pot_value)))
        
    #Neopixel
    np[0] = (r, g, b)
    np[1] = (r, g, b)
    np[2] = (r, g, b)
    np.show()    
    
        


