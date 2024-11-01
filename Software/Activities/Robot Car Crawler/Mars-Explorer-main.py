#Mars Explorer Project
from microbit import *
from picobricks import *

# Function Initialization
motor = motordriver()
pin15.set_pull(pin15.PULL_UP)
ir = IRM()

motor.dc(1,0,1)
motor.dc(2,0,1)

def forward():
    motor.dc(1,255,1)
    motor.dc(2,255,1)
    
def backward():
    motor.dc(1,255,0)
    motor.dc(2,255,0)

def left():
    motor.dc(1,0,1)
    motor.dc(2,255,1)
    
def right():
    motor.dc(1,255,1)
    motor.dc(2,0,1)

def stop():
    motor.dc(1,0,1)
    motor.dc(2,0,1)

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
    distance = measure_distance()
    #print(distance)
    key=ir.get(pin15)
    if(key!=-1):
        print(key)
        if key ==  24:
            if distance<=15:
                stop()
            else:
                forward()
                down_image()
        elif key == 90:
            right()
            right_image()
        elif key == 8:
            left()
            left_image()
        elif key == 82:
            backward()
            up_image()
        #sleep(100)
        else:
            stop()
            print(key)
            display.show(Image.HAPPY)
            
                
            
