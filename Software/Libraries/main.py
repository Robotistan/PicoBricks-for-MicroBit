from microbit import *
from picobricks import *
from touchsensor import *
import neopixel
import music
import gc

# Pin Initialization
LDR_Pin = pin0
Pot_Pin = pin1
Button_Pin = pin2
Motion_Pin = pin13
RGB_Pin = pin8
Relay_Pin = pin16
Num_Leds = 3

# Function Initialization
oled = SSD1306()
oled.init()
motor = motordriver()
shtc = SHTC3()
apds = APDS9960()
#apds.init_gesture_sensor()
apds.init_color_sensor()
gc.collect()
np = neopixel.NeoPixel(RGB_Pin, Num_Leds)
pin15.set_pull(pin15.PULL_UP)
ir = IRM()
touchsensor = CY8CMBR3116()
touchsensor.init()

#Relay
Relay_Pin.write_digital(1)
sleep(2000)
Relay_Pin.write_digital(0)

#Neopixel
np[0] = (0, 0, 255)
np[1] = (0, 255, 0)
np[2] = (255, 0, 0)
np.show()

motor.servo(1,90)
motor.dc(1,255,1)
oled.clear()

while True:
    #color = apds.read_color()
    #print(color)
    #gesture = apds.read_gesture()
    #print(gesture)

    key=ir.get(pin15)
    if(key!=-1):
        print(key)

    #LDR
    light = LDR_Pin.read_analog()
    #print(light)
    
    #Pot
    pot = Pot_Pin.read_analog()
    #print(pot)

    #Motion Sensor
    read_motion = Motion_Pin.read_digital()
    #print(read_motion)
    
    #Button
    button = Button_Pin.read_digital()
    #print(button)
    if button == 1:
        music.pitch(440)
        sleep(500)
        music.stop()

    #Temperature
    temp = shtc.temperature()
    #print(temp)

    #Humidity
    hum = shtc.humidity()
    #print(hum)

    oled.add_text(0,0,"Temp:")
    oled.add_text(6,0,str(float(temp)))
    oled.add_text(0,1,"Hum:")
    oled.add_text(6,1,str(float(hum)))
    oled.add_text(0,2,"Light:")
    oled.add_text(6,2,str(int(light)))
    oled.add_text(0,3,"Pot:")
    oled.add_text(6,3,str(float(pot * 3.3 / 1024))) 
