from microbit import *
from touchsensor import *

touchsensor = CY8CMBR3116()
touchsensor.init()

while True:
    touchsensor.PlayPiano()
    data = touchsensor.ReadButton()
    #print(data)
    if data == 7:
        display.show('C')
    elif data == 8:
        display.show('D')
    elif data == 9:
        display.show('E')
    elif data == 10:
        display.show('F')
    elif data == 11:
        display.show('G')
    elif data == 12:
        display.show('A')
    elif data == 13:
        display.show('B')
    elif data == 14:
        display.show('C')

    
        
        