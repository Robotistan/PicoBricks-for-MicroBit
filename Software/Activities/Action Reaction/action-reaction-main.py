#Blink Project
from microbit import *
from picobricks import *

# Pin Initialization
Button_Pin = pin2

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
oled.add_text(0,0,"Hello World")

#smile images
pb_smile = [
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
]
#blink images
pb_blink = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
]

while True:
    button = Button_Pin.read_digital()
    if button == 1:
        for y in range(5):
            for x in range(5):
                if pb_blink[y][x] == 1:
                    display.set_pixel(x, y, 9)
                else:
                    display.set_pixel(x, y, 0)
    else:
        for y in range(5):
            for x in range(5):
                if pb_smile[y][x] == 1:
                    display.set_pixel(x, y, 9)
                else:
                    display.set_pixel(x, y, 0)

        
        
        
    
    
