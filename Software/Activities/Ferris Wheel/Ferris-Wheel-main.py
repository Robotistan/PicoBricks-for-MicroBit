#Ferris Wheel Project
from microbit import *
from picobricks import *

# Pin Initialization
Pot_Pin = pin1

# Function Initialization
motor = motordriver()

display.show(Image.HAPPY)

while True:
    pot = Pot_Pin.read_analog()
    speed=round(round( pot - 0 ) * ( 255 - 0 ) / ( 1023 - 0 ) + 0)
    motor.dc(1,speed,1)
    
    






                    
                    
            
            
            
            
            
        
            
        
    
 
    
    
        
        
        
    
        

        




