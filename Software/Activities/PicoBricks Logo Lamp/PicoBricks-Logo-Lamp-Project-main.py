#PicoBricks Logo Lamp Project
from microbit import *
from picobricks import *
import neopixel
import random

# Pin Initialization
RGB_Pin = pin8
Num_Leds = 11 #Enter the number of LEDs
        
# Function Initialization
np = neopixel.NeoPixel(RGB_Pin, Num_Leds)

#Neopixel
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np.show()

display.show(Image.HAPPY)

r=[18,128,62,188,139,255]
g=[168,135,177,0,50,60]
b=[168,193,136,0,0,0]

while True:
    randColor=random.randint(0, 5)
    for i in range(11):
        Num_Leds=i
        np[i] = (r[randColor], g[randColor], b[randColor])
        np.show()
        sleep(100)

    






                    
                    
            
            
            
            
            
        
            
        
    
 
    
    
        
        
        
    
        

        




