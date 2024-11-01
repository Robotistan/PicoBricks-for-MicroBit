#Trash Tech Project
from microbit import *
from picobricks import *

# Function Initialization
motor = motordriver()

display.show(Image.HAPPY)
while True:
    distance = measure_distance()
    if distance<9 and distance>1:
        display.show(Image.YES)
        motor.servo(1,90)
        sleep(2000)
        motor.servo(1,180)
        sleep(200)
    else:
        motor.servo(1,180)
        display.show(Image.HAPPY)
    sleep(200)

            
                
            
