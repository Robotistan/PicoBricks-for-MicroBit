from microbit import *
import music

CHIP_ADDRESS = 0x37
PROX_STAT = b'\xAE'
CTRL_CMD = b'\x86'
BUTTON_STATUS = b'\xAA'
SAVE_CHECK_CRC = b'\x02'
SW_RESET = b'\xFF'

buff2 = bytearray(2)
proximityCounter = 0
proximityStatus = 0
tone = 0
volume = 1

NOTE_B0 = 31
NOTE_C1 = 33
NOTE_CS1 = 35
NOTE_D1 = 37
NOTE_DS1 = 39
NOTE_E1 = 41
NOTE_F1 = 44
NOTE_FS1 = 46
NOTE_G1 = 49
NOTE_GS1 = 52
NOTE_A1 = 55
NOTE_AS1 = 58
NOTE_B1 = 62
NOTE_C2 = 65
NOTE_CS2 = 69
NOTE_D2 = 73
NOTE_DS2 = 78
NOTE_E2 = 82
NOTE_F2 = 87
NOTE_FS2 = 93
NOTE_G2 = 98
NOTE_GS2 = 104
NOTE_A2 = 110
NOTE_AS2 = 117
NOTE_B2 = 123
NOTE_C3 = 131
NOTE_CS3 = 139
NOTE_D3 = 147
NOTE_DS3 = 156
NOTE_E3 = 165
NOTE_F3 = 175
NOTE_FS3 = 185
NOTE_G3 = 196
NOTE_GS3 = 208
NOTE_A3 = 220
NOTE_AS3 = 233
NOTE_B3 = 247
NOTE_C4 = 262
NOTE_CS4 = 277
NOTE_D4 = 294
NOTE_DS4 = 311
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_FS4 = 370
NOTE_G4 = 392
NOTE_GS4 = 415
NOTE_A4 = 440
NOTE_AS4 = 466
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_CS5 = 554
NOTE_D5 = 587
NOTE_DS5 = 622
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_FS5 = 740
NOTE_G5 = 784
NOTE_GS5 = 831
NOTE_A5 = 880
NOTE_AS5 = 932
NOTE_B5 = 988
NOTE_C6 = 1047
NOTE_CS6 = 1109
NOTE_D6 = 1175
NOTE_DS6 = 1245
NOTE_E6 = 1319
NOTE_F6 = 1397
NOTE_FS6 = 1480
NOTE_G6 = 1568
NOTE_GS6 = 1661
NOTE_A6 = 1760
NOTE_AS6 = 1865
NOTE_B6 = 1976
NOTE_C7 = 2093
NOTE_CS7 = 2217
NOTE_D7 = 2349
NOTE_DS7 = 2489
NOTE_E7 = 2637
NOTE_F7 = 2794
NOTE_FS7 = 2960
NOTE_G7 = 3136
NOTE_GS7 = 3322
NOTE_A7 = 3520
NOTE_AS7 = 3729
NOTE_B7 = 3951
NOTE_C8 = 4186
NOTE_CS8 = 4435
NOTE_D8 = 4699
NOTE_DS8 = 4978

button_X = 1
button_Y = 2
left_button = 3
right_button = 4
up_button = 5
down_button = 6
button_C1 = 7
button_D = 8
button_E = 8
button_F = 9
button_G = 10
button_A = 11
button_B = 12
button_C2 = 13

class CY8CMBR3116:
    def init(self):    
        # OFFSET
        buff2[0] = 0x00
        buff2[1] = 0x00
        try:
            i2c.write(CHIP_ADDRESS, buff2) 
        except:  
            print("1")
        try:
            i2c.write(CHIP_ADDRESS, buff2) 
        except:  
            print("2")
        try:
            i2c.write(CHIP_ADDRESS, buff2) 
        except:  
            print("3")
        try:
            i2c.write(CHIP_ADDRESS, buff2) 
        except:  
            print("4")
    
        i2c.write(CHIP_ADDRESS, b'\x00\xFF\x7F\xFE\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x0E\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x03\x00\x00')
        i2c.write(CHIP_ADDRESS, b'\x1F\x00\x00\x00\x00\x00\x00\x00\x01\x81\x06\x00\x00\xFF\xF0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        i2c.write(CHIP_ADDRESS, b'\x3E\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x03\x01\x58\x00\x37\x06\x00\x00\x0A\x00\x00\x00\x00\x00\x00\x00')
        i2c.write(CHIP_ADDRESS, b'\x5D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        i2c.write(CHIP_ADDRESS, b'\x7C\x00\x00\x87\x04')
        i2c.write(CHIP_ADDRESS, b'\x86\x02')
        sleep(200)
        i2c.write(CHIP_ADDRESS, b'\x86\xFF')
        sleep(200)
        
    def PlayPiano(self):
        global proximityCounter
        global proximityStatus 
        global val
        global tone
        global volume
    
        i2c.write(CHIP_ADDRESS, PROX_STAT)
        val = i2c.read(CHIP_ADDRESS, 1)
        
        i2c.write(CHIP_ADDRESS, BUTTON_STATUS)
        buff = i2c.read(CHIP_ADDRESS, 2)
    
        if ((val[0] & 0x01) != 0):
            if (++proximityCounter > 30) :
                proximityStatus = 1
                proximityCounter = 0
            
        else:
            proximityCounter = 0
            proximityStatus = 0
    
        if ((buff[0] & 0x80) != 0) : # left button
            music.pitch(NOTE_D4)
            tone -= 1
        
        if ((buff[0] & 0x20) != 0) : # right button
            music.pitch(NOTE_D4)
            tone += 1
        
        if ((buff[0] & 0x10) != 0) : # top button
            music.pitch(NOTE_D4)
            volume += 1
        
        if ((buff[0] & 0x40) != 0) : # down button
            music.pitch(NOTE_D4)
            volume -= 1
            
        if(tone <= 0):
            tone = 0
        if(tone >= 1):
            tone =1
    
        if (volume <= 0):
            volume = 0
        if (volume >= 1):
            volume = 1
    
        if(volume == 0):
            set_volume(100)
            
        if (volume == 1):
            set_volume(255)
    
        if ((buff[0] & 0x08) != 0) : #C1
            if (tone == 0):
                music.pitch(NOTE_C4)
            
            elif (tone == 1):
                music.pitch(NOTE_C5)
            
        if ((buff[1] & 0x40) != 0) : #D
            if (tone == 0) :
                music.pitch(NOTE_D4)
            
            elif (tone == 1) :
                music.pitch(NOTE_D5)
            
        if ((buff[1] & 0x20) != 0) : #E
            if (tone == 0) :
                music.pitch(NOTE_E4)
             
            elif (tone == 1) :
                music.pitch(NOTE_E5)
            
        if ((buff[1] & 0x10) != 0) : #F
            if (tone == 0) :
                music.pitch(NOTE_F4)   
            
            elif (tone == 1) :
                music.pitch(NOTE_F5)
        
        if ((buff[1] & 0x08) != 0) : #G
            if (tone == 0) :
                music.pitch(NOTE_G4) 
             
            elif (tone == 1) :
                music.pitch(NOTE_G5) 
        
        if ((buff[1] & 0x04) != 0) : #A
            if (tone == 0) :
                music.pitch(NOTE_A4) 
              
            elif (tone == 1) :
                music.pitch(NOTE_A5)
        
        if ((buff[1] & 0x02) != 0) : #B
            if (tone == 0) :
                music.pitch(NOTE_B4)   
            
            elif (tone == 1) :
                music.pitch(NOTE_B5)
        
        if ((buff[1] & 0x01) != 0) : #C2
            if (tone == 0) :
                music.pitch(NOTE_C5)  
            
            elif (tone == 1) :
                music.pitch(NOTE_C6) 
        
        if (((buff[1] & 0x08) == 0) and ((buff[1] & 0xFF) == 0) and ((buff[0] & 0x08) == 0) and ((buff[0] & 0xFF) == 0)) :
            music.stop()
    
    button_A = 14
    button_B = 1
    left_button = 2
    right_button = 3
    up_button = 4
    down_button = 5
    middle_C = 6
    
    middle_D = 7
    middle_E = 8
    middle_F = 9
    middle_G = 10
    middle_A = 11
    middle_B = 12
    high_C   = 13
    
    def ReadButton(self):
        global proximityCounter
        global proximityStatus
    
        value = 0
    
        try:
            i2c.write(CHIP_ADDRESS, PROX_STAT)
        except:
            pass
        try:
            i2c.write(CHIP_ADDRESS, PROX_STAT)
        except:
            pass
            
        val = i2c.read(CHIP_ADDRESS, 1)
        
        i2c.write(CHIP_ADDRESS, BUTTON_STATUS)
        buff = i2c.read(CHIP_ADDRESS, 2)
        if ((val[0] & 0x01) != 0):
            if (++proximityCounter > 30) :
                proximityStatus = 1
                proximityCounter = 0
            
        else:
            proximityCounter = 0
            proximityStatus = 0
    
        if ((buff[0] & 0x02) != 0) : #A Button
            value = button_X
            print("X PRESSED")
             
        if ((buff[0] & 0x04) != 0) : #b Button
            value = button_Y
            print("Y PRESSED")
    
        if ((buff[0] & 0x80) != 0) : #left Button
            value = left_button
            print("Left button PRESSED")
        if ((buff[0] & 0x20) != 0) : #right Button
            value = right_button
            print("right button PRESSED")  
        if ((buff[0] & 0x10) != 0) : #up Button
            value = right_button
            print("up button PRESSED")
        if ((buff[0] & 0x40) != 0) : #down Button
            value = down_button
            print("down button PRESSED")
            
        if ((buff[0] & 0x08) != 0) : #C1
            value = button_C1
            print("C1 button PRESSED")
    
        if ((buff[1] & 0x40) != 0) : #D
            value = button_D
            print("D button PRESSED")
        if ((buff[1] & 0x20) != 0) : #E
            value = button_E
            print("E button PRESSED")
        if ((buff[1] & 0x10) != 0) : #F
            value = button_F
            print("F button PRESSED")
        if ((buff[1] & 0x08) != 0) : #G
            value = button_G
            print("G button PRESSED")
        if ((buff[1] & 0x04) != 0) : #A
            value = button_A
            print("A button PRESSED")
        if ((buff[1] & 0x02) != 0) : #B
            value = button_B
            print("B button PRESSED")
        if ((buff[1] & 0x01) != 0) : #C2
            value = button_C2
            print("C2 button PRESSED")
            
        return value
