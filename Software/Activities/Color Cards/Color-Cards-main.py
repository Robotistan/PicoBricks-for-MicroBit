#Color Cards Project
from microbit import *
from picobricks import *
import neopixel
import gc

RGB_Pin = pin8  # Pin connected to the NeoPixel strip
Num_Leds = 3    # Number of LEDs in the strip

# Initialize the APDS9960 color sensor
apds = APDS9960()
apds.init_color_sensor()
gc.collect()  # Collect garbage to free up memory

# Initialize the NeoPixel strip
np = neopixel.NeoPixel(RGB_Pin, Num_Leds)

while True:
    # Read the RGB values from the color sensor
    r_color = apds.color_value("red") or 0
    sleep(100)
    g_color = apds.color_value("green") or 0
    sleep(100)
    b_color = apds.color_value("blue") or 0
    sleep(100)
    
    print("red")
    print(r_color)
    print("green")
    print(g_color)
    print("blue")
    print(b_color)
    
    r=round(round( r_color - 0 ) * ( 255 - 0 ) / ( 1023 - 0 ) + 0)
    g=round(round( g_color - 0 ) * ( 255 - 0 ) / ( 1023 - 0 ) + 0)
    b=round(round( b_color - 0 ) * ( 255 - 0 ) / ( 1023 - 0 ) + 0)

    # Set the color of the NeoPixels
    np[0] = (r, g, b)
    np[1] = (r, g, b)
    np[2] = (r, g, b)
    np.show()  # Update the NeoPixels to show the new colors
    sleep(100)  # Wait for half a second before the next update