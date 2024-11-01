#Gesture Controlled Arm Pantilt Project
from microbit import *
from picobricks import *
import music
        
# Function Initialization
apds = APDS9960()
apds.init_gesture_sensor()
motor = motordriver()

motor.servo(1,0)
motor.servo(2,0)

display.show(Image.YES)

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

def up_image():
    display.show(Image('00900:'
                       '09990:'
                       '90909:'
                       '00900:'
                       '00900'))

def down_image():
    display.show(Image('00900:'
                       '00900:'
                       '90909:'
                       '09990:'
                       '00900'))
    
while True:
    gesture = apds.read_gesture()
    if gesture=="RIGHT":
        motor.servo(1,0)
        right_image()
        music.play(['c'])
    elif gesture=="LEFT":
        motor.servo(1,180)
        left_image()
        music.play(['c'])
    elif gesture=="UP":
        motor.servo(2,0)
        up_image()
        music.play(['c'])
    elif gesture=="DOWN":
        motor.servo(2,180)
        down_image()
        music.play(['c'])
    elif button_a.is_pressed():
        motor.servo(1,0)
        motor.servo(2,0)
        display.show(Image.YES)
        
        
        
        

    






                    
                    
            
            
            
            
            
        
            
        
    
 
    
    
        
        
        
    
        

        



