#Money Box Project
from microbit import *
from picobricks import *

# Function Initialization
motor = motordriver()
motor.servo(1,180)

trashDetected=0
distance=100

while True:
    rawdistance=measure_distance()
    if rawdistance<1200:
        distance=rawdistance
    motor.servo(1,180)
    sleep(500)
    if distance<5:
        trashDetected=1
        sleep(300)
    if distance>9 and trashDetected==1:
        trashDetected=0
        motor.servo(1,90)
        sleep(500)

            
                
            
