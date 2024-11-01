#Morse Code Cryptography
from microbit import *
from picobricks import *
import neopixel

# Pin Initialization
RGB_Pin = pin8
Num_Leds = 3

# Function Initialization
oled = SSD1306()
oled.init()
oled.clear()
np = neopixel.NeoPixel(RGB_Pin, Num_Leds)

#Neopixel
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np.show()

morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
         '.---', '-.-','.-..','--', '-.','---', '.--.', '--.-',
         '.-.', '...','-','..-', '...-', '.--','-..-', '-.--',
         '--..', '.----','..---','...--','....-','.....', '-....',
         '--...','---..', '----.','-----']

alphabet = ['a','b','c','d','e','f','g','h','i',
         'j', 'k','l','m', 'n','o', 'p', 'q',
         'r', 's','t','u', 'v', 'w','x', 'y',
         'z', '1','2','3','4','5', '6',
         '7','8', '9','0']

#print(len(alphabet))                
while True:
    if button_a.is_pressed():
        passwordText="picobricks"
        for i in range((len(passwordText))):
            oled.clear()
            oled.add_text(0,0,str(passwordText))
            display.show(passwordText[i])
            oled.add_text(0,1,str(morse[alphabet.index(passwordText[i])]))

            j=0
            for j in range(len(morse[alphabet.index(passwordText[i])])):
                oled.add_text(0,2,str(morse[alphabet.index(passwordText[i])][j]))
                if morse[alphabet.index(passwordText[i])][j] == '.' :
                    np[0] = (255, 255, 255)
                    np[1] = (255, 255, 255)
                    np[2] = (255, 255, 255)
                    np.show()
                    sleep(500)
                else:
                    np[0] = (255, 255, 255)
                    np[1] = (255, 255, 255)
                    np[2] = (255, 255, 255)
                    np.show()
                    sleep(1500)
                np[0] = (0, 0, 0)
                np[1] = (0, 0, 0)
                np[2] = (0, 0, 0)
                np.show()
                sleep(100)
                    
                    
            
            
            
            
            
        
            
        
    
 
    
    
        
        
        
    
        

        



