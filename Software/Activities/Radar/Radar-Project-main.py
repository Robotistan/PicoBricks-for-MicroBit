#PicoBricks Radar Project
from microbit import *
from picobricks import *
import music

# Pin Initialization
Button_Pin = pin2
Pot_Pin = pin1

# Function Initialization
oled = SSD1306()
oled.init()
motor = motordriver()

motor.servo(1,90)
angleServo=0
radarRange=0
c=1
button = Button_Pin.read_digital()
while Button_Pin.read_digital()==0:
    oled.clear() 
    pot = Pot_Pin.read_analog()
    radarRange=round(round( pot - 0 ) * ( 100 - 0 ) / ( 1023 - 0 ) + 0)
    oled.add_text(0,0,"Radar Range:")
    oled.add_text(5,1,str(radarRange))
    sleep(50)
oled.clear()

while True:
    oled.clear()
    distance = measure_distance()
    while round(measure_distance())>= radarRange:
        oled.add_text(2,2,"Scaning...")
        motor.servo(1,angleServo)
        if c==1:
            angleServo=angleServo+5
        if c==0:
            angleServo=angleServo-5
        if angleServo==180:
            c=0
        if angleServo==0:
            c=1
        sleep(10)
    oled.clear()
    objectDistance=round(distance)
    oled.add_text(2,0,"Object")
    oled.add_text(2,1,"Detected!")
    oled.add_text(0,2,"cm:")
    oled.add_text(5,2,str(objectDistance))
    oled.add_text(0,3,"Degreess")
    oled.add_text(8,3,str(angleServo))
    music.play(['c'])
    
    

        
        
    



   
        
            
    

