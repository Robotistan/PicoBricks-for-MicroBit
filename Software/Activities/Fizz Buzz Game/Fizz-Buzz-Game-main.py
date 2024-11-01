#Fizz-Buzz Game Projects
from microbit import *
from picobricks import *
import neopixel
import music

# Pin Initialization
Button_Pin = pin2
RGB_Pin = pin8
Num_Leds = 3

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
np = neopixel.NeoPixel(RGB_Pin, Num_Leds)

button = Button_Pin.read_digital()
display.show(Image.HEART)

oled.add_text(2,0,"Press the")
oled.add_text(1,1,"A Button to")
oled.add_text(3,2,"start")
oled.add_text(2,3,"Fizz-Buzz")

def left_image():
    display.show(Image('00900:'
                       '09000:'
                       '99999:'
                       '09000:'
                       '00900'))
#Neopixel
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np.show()

while True:
    if button_a.is_pressed():
        oled.clear()
        counter=1
        left_image()
        while counter<100:
            oled.add_text(0,0,"Press the PB")
            oled.add_text(3,1,"Button")
            oled.add_text(5,2,str(counter))
            button = Button_Pin.read_digital()
            if button==1:
                counter=counter+1
                music.play(['b'])
                oled.add_text(3,3,"         ")
                np[0] = (0, 0, 0)
                np[1] = (0, 0, 0)
                np[2] = (0, 0, 0)
                np.show()
            if counter % 3 == 0:
                oled.add_text(3,3,"Fizz")
                np[0] = (255, 0, 0)
                np[1] = (255, 0, 0)
                np[2] = (255, 0, 0)
                np.show()
            if counter % 5 == 0:
                oled.add_text(3,3,"Buzz")
                np[0] = (0, 0, 255)
                np[1] = (0, 0, 255)
                np[2] = (0, 0, 255)
                np.show()
            if counter % 15 == 0:
                oled.add_text(3,3,"Fizz-Buzz")
                np[0] = (128, 0, 128)
                np[1] = (128, 0, 128)
                np[2] = (128, 0, 128)
                np.show()
                
                
            
        
    
 
    
    
        
        
        
    
        

        


