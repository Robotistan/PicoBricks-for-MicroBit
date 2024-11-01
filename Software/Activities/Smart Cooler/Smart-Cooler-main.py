#Smart Cooler Project
from microbit import *
from picobricks import *

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
shtc = SHTC3()
motor = motordriver()

def celsius():
    display.show(Image('00009:'
                       '09900:'
                       '90000:'
                       '90000:'
                       '09900'))
celsius()

while True:
    temp = shtc.temperature()
    hum=shtc.humidity()
    oled.add_text(0,0,"TEMP:")
    oled.add_text(5,0,str(float(temp)))
    oled.add_text(0,1,"HUM:")
    oled.add_text(5,1,str(float(hum)))
    
    motorSpeed=round( shtc.temperature() - 0 ) * ( 100 - 0 ) / ( 40 - 0 ) + 0
    if temp>25:
        motor.dc(1,round(motorSpeed),1)
        oled.add_text(0,2,"Fan Speed:")
        oled.add_text(5,3,str(round(motorSpeed)))
    else:
        motor.dc(1,0,1)
    
        
        
        
    
        

        



