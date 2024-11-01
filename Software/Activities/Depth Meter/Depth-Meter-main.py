#Depth Meter Projects
from microbit import *
from picobricks import *

# Pin Initialization
Pot_Pin = pin1
Button_Pin = pin2

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
motor = motordriver()
button = Button_Pin.read_digital()

while button_a.is_pressed()==0:
    oled.clear()
    glassDeepValue=10
    oled.add_text(2,0,"Press the")
    oled.add_text(3,1,"A Button")
    oled.add_text(5,2,str(glassDeepValue))
    sleep(100)

while True:
    oled.clear()
    distance = measure_distance()
    print(distance)
    waterDeepValue=glassDeepValue-round(distance)
    oled.add_text(0,2,"Depth:")
    oled.add_text(8,2,str(waterDeepValue))
    if waterDeepValue<(glassDeepValue-4):
        motor.dc(1,150,1)
    else:
        motor.dc(1,0,1)
    sleep(100)

    
 
    
    
        
        
        
    
        

        





        
        
        
    
    
