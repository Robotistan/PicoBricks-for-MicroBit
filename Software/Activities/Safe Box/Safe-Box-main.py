#Safe Box Project
from microbit import *
from picobricks import *

# Pin Initialization
LDR_Pin = pin0
Pot_Pin = pin1
Button_Pin = pin2

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
motor = motordriver()

display.show(Image.HAPPY)
password=[1,2,3,4]
userPass=[]

def startOLED():
    oled.add_text(0,1,"Close the lid")
    oled.add_text(0,2,"to lock the")
    oled.add_text(0,3,"SafeBox")
    
def addList():
    #counter=0
    if counter>0:
        oled.add_text(2,3,str(userPass[0]))
    if counter>1:
        oled.add_text(4,3,str(userPass[1]))
    if counter>2:
        oled.add_text(6,3,str(userPass[2]))
    if counter>3:
        oled.add_text(8,3,str(userPass[3]))

def controlLoop():
    control=0
    for i in range(4):
        if password[i]!=userPass[i] :
            control=1
    if control==1:
        display.show(Image.NO)
    else:
        display.show(Image.YES)
        motor.servo(1,90)
        sleep(3000)
        oled.clear()
            
        
                
while True:
    display.show(Image.HAPPY)
    counter=0
    startOLED()
    light = LDR_Pin.read_analog()
    pot = Pot_Pin.read_analog()
    button = Button_Pin.read_digital()
    print(light)
    if light<50:
        sleep(2000)
        oled.clear()
        motor.servo(1,180)
        while counter<4:
            pot = Pot_Pin.read_analog()
            userNumber=round(round( pot - 0 ) * ( 9 - 0 ) / ( 1023 - 0 ) + 0)
            oled.add_text(2,1,"Password:")
            oled.add_text((2+(counter*2)),3,str(userNumber))
            addList()
            button = Button_Pin.read_digital()
            if button==1:
                userPass.insert(counter,userNumber)
                counter=counter+1
                sleep(200)

        controlLoop()
    sleep(500)
    counter=0
    control=0
            
                
            
        
    
    
    
    
    






                    
                    
            
            
            
            
            
        
            
        
    
 
    
    
        
        
        
    
        

        





