#Night and Day Projects
from microbit import *
from picobricks import *
import neopixel
import random
import music

# Pin Initialization
LDR_Pin = pin0
Button_Pin = pin2
RGB_Pin = pin8
Num_Leds = 3

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
np = neopixel.NeoPixel(RGB_Pin, Num_Leds)

counter=0
falseValue=0

button = Button_Pin.read_digital()

while Button_Pin.read_digital()==0:
    oled.add_text(0,1,"Press BUTTON")
    oled.add_text(2,2,"to START!")
    
oled.clear()
while counter!=100 and falseValue==0:
    light = LDR_Pin.read_analog()
    rand=random.randint(1, 2)
    if rand==1:
        oled.add_text(0,0,"NIGHT")
    else:
        oled.add_text(0,0,"DAY")
    sleep(3000)
    light = LDR_Pin.read_analog()
    if light<60 and rand==1:
        display.show(Image.YES)
        counter=counter+10
    elif light>60 and rand==1:
        display.show(Image.NO)
        falseValue=1
    elif light>60 and rand==2:
        display.show(Image.YES)
        counter=counter+10
    else:
        display.show(Image.NO)
        falseValue=1
    oled.clear()
if counter==100:
    oled.add_text(0,0,"Congrats!!!")
    oled.add_text(0,1,"Top Score:")
    oled.add_text(5,2,str(counter))
    music.play(music.WEDDING)
else:
    oled.add_text(0,0,"Game Over")
    oled.add_text(0,1,"Score:")
    oled.add_text(5,2,str(counter))
    
 
    
    
        
        
        
    
        

        


