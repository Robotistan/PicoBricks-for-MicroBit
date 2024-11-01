#Coin Dispenser Project
from microbit import *
from picobricks import *
        
# Function Initialization
apds = APDS9960()
apds.init_gesture_sensor()
motor = motordriver()

display.show(Image.HAPPY)

def left_image():
    display.show(Image('00900:'
                       '09000:'
                       '99999:'
                       '09000:'
                       '00900'))

def right_image():
    display.show(Image('00900:'
                       '00090:'
                       '99999:'
                       '00090:'
                       '00900'))
    
while True:
    gesture = apds.read_gesture()
    if gesture=="RIGHT":
        right_image()
        motor.servo(1,180)
    elif gesture=="LEFT":
        left_image()
        motor.servo(1,0)
        

    






                    
                    
            
            
            
            
            
        
            
        
    
 
    
    
        
        
        
    
        

        



