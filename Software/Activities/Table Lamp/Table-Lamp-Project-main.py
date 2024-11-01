#Table Lamp Project
from microbit import *
from picobricks import *
import neopixel

# Pin Initialization
RGB_Pin = pin8
Num_Leds = 3 #Enter the number of LEDs
        
# Function Initialization
apds = APDS9960()
apds.init_gesture_sensor()
np = neopixel.NeoPixel(RGB_Pin, Num_Leds)

#Neopixel
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np.show()

colorCounter=0
display.show(Image.HAPPY)
r=[255,128,188,62,139,255,18]
g=[255,135,0,177,50,60,168]
b=[255,193,0,136,0,0,168]

while True:
    gesture = apds.read_gesture()
    if gesture=="RIGHT":
        np[0] = (r[colorCounter], g[colorCounter], b[colorCounter])
        np[1] = (r[colorCounter], g[colorCounter], b[colorCounter])
        np[2] = (r[colorCounter], g[colorCounter], b[colorCounter])
        np.show()
        display.show(Image.HEART)       
    elif gesture=="LEFT":
        display.show(colorCounter)
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np.show()
    elif gesture=="UP":
        colorCounter=colorCounter-1
        if colorCounter<0:
            colorCounter=6
        display.show(colorCounter)
    elif gesture=="DOWN":
        colorCounter=colorCounter+1
        if colorCounter>6:
            colorCounter=0
        display.show(colorCounter)
    






                    
                    
            
            
            
            
            
        
            
        
    
 
    
    
        
        
        
    
        

        



