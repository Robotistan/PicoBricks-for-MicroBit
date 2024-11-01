#Thermometer Project
from microbit import *
from picobricks import *

# Pin Initialization
Pot_Pin = pin1

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
shtc = SHTC3()

oled.add_text(0,0,"TEMP:")
oled.add_text(0,1,"_______________")
oled.add_text(0,3,"HUM:")

def celsius():
    display.show(Image('00009:'
                       '09900:'
                       '90000:'
                       '90000:'
                       '09900'))
def Fahrenheit():
    display.show(Image('99909:'
                       '90000:'
                       '99900:'
                       '90000:'
                       '90000'))
    
while True:
    
    temp = shtc.temperature()
    hum=shtc.humidity()
    pot_value = round(round( Pot_Pin.read_analog() - 0 ) * ( 2 - 1 ) / ( 1023 - 0 ) + 1)
    if pot_value==1:
        celsius()
        temp=round(shtc.temperature())
    else:
        Fahrenheit()
        temp=round((9*shtc.temperature())/5 + 32)
    oled.add_text(5,0,str(temp))
    oled.add_text(5,3,str(round(hum)))
        
        
        
        
    
        

        



