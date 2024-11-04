#Car Parking System
from microbit import *
from picobricks import *

motor = motordriver()
motor.servo(1,90)

while True:
    distance = measure_distance()
    #print(distance)
    if round(distance)<6:
        motor.servo(1,180)
        display.show(Image.YES)
        sleep(1000)
    else:
        display.show(Image.NO)
        motor.servo(1,180)
        
        
        




                    
                    
            
            
            
            
            
        
            
        
    
 
    
    
        
        
        
    
        

        



