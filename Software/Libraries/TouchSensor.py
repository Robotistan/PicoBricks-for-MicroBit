from microbit import i2c
from microbit import *
import music

CHIP_ADDRESS = 0x37

buf = bytearray(2)
proximityCounter = 0
proximityStatus = 0
tone = 0
volume = 1

def touchinit():    
    # OFFSET
    buf[0] = 0x00
    buf[1] = 0x00
    try:
        i2c.write(CHIP_ADDRESS, buf) 
    except:  
        pass
    try:
        i2c.write(CHIP_ADDRESS, buf) 
    except:  
        pass
    try:
        i2c.write(CHIP_ADDRESS, buf) 
    except:  
        pass
    try:
        i2c.write(CHIP_ADDRESS, buf) 
    except:  
        pass

    i2c.write(CHIP_ADDRESS, b'\x00\xFF\x7F\xFE\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x0E\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x03\x00\x00')
    i2c.write(CHIP_ADDRESS, b'\x1F\x00\x00\x00\x00\x00\x00\x00\x01\x81\x06\x00\x00\xFF\xF0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    i2c.write(CHIP_ADDRESS, b'\x3E\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x03\x01\x58\x00\x37\x06\x00\x00\x0A\x00\x00\x00\x00\x00\x00\x00')
    i2c.write(CHIP_ADDRESS, b'\x5D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    i2c.write(CHIP_ADDRESS, b'\x7C\x00\x00\x87\x04')
    i2c.write(CHIP_ADDRESS, b'\x86\x02')
    sleep(200)
    i2c.write(CHIP_ADDRESS, b'\x86\xFF')
    sleep(200)
    
def play_piano():
    global proximityCounter, proximityStatus, buff2, tone, volume

    try:
        i2c.write(CHIP_ADDRESS, b'\x00\x00') 
    except:  
        pass
    try:
        i2c.write(CHIP_ADDRESS, b'\x00\x00') 
    except:  
        pass
    try:
        i2c.write(CHIP_ADDRESS, b'\x00\x00') 
    except:  
        pass
    try:
        i2c.write(CHIP_ADDRESS, b'\x00\x00') 
    except:  
        pass

    i2c.write(CHIP_ADDRESS, b'\xAE')#PROX_STAT
    val = i2c.read(CHIP_ADDRESS, 1)
    print(val)
    i2c.write(CHIP_ADDRESS, b'\xAA')#BUTTON_STATUS
    buf = i2c.read(CHIP_ADDRESS, 2)
    
    if ((val[0] & 0x01) != 0):
        if (++proximityCounter > 30) :
            proximityStatus = 1
            proximityCounter = 0
        
    else:
        proximityCounter = 0
        proximityStatus = 0

    if ((buf[0] & 0x80) != 0) : #Left Button
        music.play(['d4'])
        tone -= 1
    if ((buf[0] & 0x20) != 0) : #Right Button
        music.play(['d4'])
        tone += 1
    if ((buf[0] & 0x10) != 0) : #Up Button
        music.play(['d4'])
        volume += 1
    if ((buf[0] & 0x40) != 0) : #Down Button
        music.play(['d4'])
        volume -= 1 

    if (tone <= 0):
        tone = 0
    else:
        tone = 1

    if (volume <= 0):
        volume = 0
    else:
        volume = 1

    if (volume == 0):
        set_volume(100)
    else:
        set_volume(255)
        
    if ((buf[0] & 0x08) != 0) : #C1
        if (tone == 0):
            music.play(['c4'])
        else:
            music.play(['c5'])
    if ((buf[1] & 0x40) != 0) : #D
        if (tone == 0):
            music.play(['d4'])
        else:
            music.play(['d5'])
    if ((buf[1] & 0x20) != 0) : #E
        if (tone == 0):
            music.play(['e4'])
        else:
            music.play(['e5'])
    if ((buf[1] & 0x10) != 0) : #F
        if (tone == 0):
            music.play(['f4'])
        else:
            music.play(['f5'])
    if ((buf[1] & 0x08) != 0) : #G
        if (tone == 0):
            music.play(['g4'])
        else:
            music.play(['g5'])
    if ((buf[1] & 0x04) != 0) : #A
        if (tone == 0):
            music.play(['a4'])
        else:
            music.play(['a5'])
    if ((buf[1] & 0x02) != 0) : #B
        if (tone == 0):
            music.play(['b4'])
        else:
            music.play(['b5'])
    if ((buf[1] & 0x01) != 0) : #C2
        if (tone == 0):
            music.play(['c5'])
        else:
            music.play(['c6'])

    if (((buf[1] & 0x08) == 0) and ((buf[1] & 0xFF) == 0) and ((buf[0] & 0x08) == 0) and ((buf[0] & 0xFF) == 0)) :
        music.stop()

def piano_touched(button): #String
    global proximityCounter, proximityStatus
    value = 0

    try:
        i2c.write(CHIP_ADDRESS, b'\x00\x00') 
    except:
        pass
    try:
        i2c.write(CHIP_ADDRESS, b'\x00\x00') 
    except:
        pass
    try:
        i2c.write(CHIP_ADDRESS, b'\x00\x00') 
    except:
        pass
    try:
        i2c.write(CHIP_ADDRESS, b'\x00\x00') 
    except:
        pass
 
    i2c.write(CHIP_ADDRESS, b'\xAE')#PROX_STAT
    val = i2c.read(CHIP_ADDRESS, 1)
    print(val)
    i2c.write(CHIP_ADDRESS, b'\xAA')#BUTTON_STATUS
    buf = i2c.read(CHIP_ADDRESS, 2)
    
    if ((val[0] & 0x01) != 0):
        if (++proximityCounter > 30) :
            proximityStatus = 1
            proximityCounter = 0
        
    else:
        proximityCounter = 0
        proximityStatus = 0

    if ((buf[0] & 0x80) != 0) : #Left Button
        value = "LEFT"
    if ((buf[0] & 0x20) != 0) : #Right Button
        value = "RIGHT"
    if ((buf[0] & 0x10) != 0) : #Up Button
        value = "UP"
    if ((buf[0] & 0x40) != 0) : #Down Button
        value = "DOWN"
    if ((buf[0] & 0x02) != 0) : #X 
        value = "X"
    if ((buf[0] & 0x04) != 0) : #Y
        value = "Y"
    if ((buf[0] & 0x08) != 0) : #C1
        value = "C1"
    if ((buf[1] & 0x40) != 0) : #D
        value = "D"
    if ((buf[1] & 0x20) != 0) : #E
        value = "E"
    if ((buf[1] & 0x10) != 0) : #F
        value = "F"
    if ((buf[1] & 0x08) != 0) : #G
        value = "G"
    if ((buf[1] & 0x04) != 0) : #A
        value = "A"
    if ((buf[1] & 0x02) != 0) : #B
        value = "B"
    if ((buf[1] & 0x01) != 0) : #C
        value = "C2"
        
    if(button == value):
        return 1
    else:
        return 0
