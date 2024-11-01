#3D Labyrinth Project
from microbit import *
from picobricks import *

# Function Initialization
oled = SSD1306()
oled.init()
motor = motordriver()
apds = APDS9960()
apds.init_gesture_sensor()
pin15.set_pull(pin15.PULL_UP)
ir = IRM()

def labyrinth_image():
    display.show(Image('90090:'
                       '99990:'
                       '00099:'
                       '99999:'
                       '00009'))
labyrinth_image()
servo1Value=45
servo2Value=45

while True:
    gesture = apds.read_gesture()
    oled.clear()
    motor.servo(1,servo1Value)
    motor.servo(1,servo2Value)
    sleep(100)
    if gesture == "UP":
        servo1Value=servo1Value-1
        if servo1Value==15:
            servo1Value=16
    if gesture == "DOWN":
        servo1Value=servo1Value+1
        if servo1Value==58:
            servo1Value=57
    if gesture == "RIGHT":
        servo2Value=servo2Value+1
        if servo2Value==80:
            servo2Value=79
    if gesture == "LEFT":
        servo2Value=servo2Value-1
        if servo2Value==30:
            servo2Value=31
    oled.add_text(0,0,str(servo1Value))
    oled.add_text(0,1,str(servo2Value))
    if button_a.is_pressed():
        labyrinth_image()
        servo1Value=45
        servo2Value=45
    gesture=0
        
            
    
