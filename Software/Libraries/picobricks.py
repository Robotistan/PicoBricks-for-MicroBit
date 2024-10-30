from microbit import *
from microbit import i2c, Image
import machine
import time

OLED_ADDRESS = 0x3C
MOTOR_DRIVER_ADDRESS = 0x22
SHTC_ADDRESS = 0x70
APDS9960_ADDRESS = 0x39
APDS9960_GESTURE_THRESHOLD_OUT = 10
APDS9960_GESTURE_SENSITIVITY_1 = 50

screen = bytearray(513)  
screen[0] = 0x40
zoom = 1

val = bytearray(2)
buf = bytearray(1)
buffer = bytearray(5)
u_data = bytearray(32)
d_data = bytearray(32)
l_data = bytearray(32)
r_data = bytearray(32)

##########Oled Library##########
class SSD1306:  
    def command(self,c):
        i2c.write(OLED_ADDRESS, b'\x00' + bytearray(c))
    
    def init(self):
        cmd = [
            [0xAE],                     # SSD1306_DISPLAYOFF
            [0xA4],                     # SSD1306_DISPLAYALLON_RESUME
            [0xD5, 0xF0],               # SSD1306_SETDISPLAYCLOCKDIV
            [0xA8, 0x3F],               # SSD1306_SETMULTIPLEX
            [0xD3, 0x00],               # SSD1306_SETDISPLAYOFFSET
            [0 | 0x0],                  # line #SSD1306_SETSTARTLINE
            [0x8D, 0x14],               # SSD1306_CHARGEPUMP
            # 0x20 0x00 horizontal addressing
            [0x20, 0x00],               # SSD1306_MEMORYMODE
            [0x21, 0, 127],             # SSD1306_COLUMNADDR
            [0x22, 0, 63],              # SSD1306_PAGEADDR
            [0xa0 | 0x1],               # SSD1306_SEGREMAP
            [0xc8],                     # SSD1306_COMSCANDEC
            [0xDA, 0x12],               # SSD1306_SETCOMPINS
            [0x81, 0xCF],               # SSD1306_SETCONTRAST
            [0xd9, 0xF1],               # SSD1306_SETPRECHARGE
            [0xDB, 0x40],               # SSD1306_SETVCOMDETECT
            [0xA6],                     # SSD1306_NORMALDISPLAY
            [0xd6, 1],                  # zoom on
            [0xaf]                      # SSD1306_DISPLAYON
        ]
        for c in cmd:
            self.command(c)
    
    def set_pos(self,col=0, page=0):
        self.command([0xb0 | page])  # page number
        # take upper and lower value of col * 2
        c1, c2 = col * 2 & 0x0F, col >> 3
        self.command([0x00 | c1])  # lower start column address
        self.command([0x10 | c2])  # upper start column address
    
    def clear(self,c=0):
        global screen
        self.set_pos()
        for i in range(1, 513):
            screen[i] = 0
        self.draw_screen()
    
    def set_zoom(self,v):
        global zoom
        if zoom != v:
            self.command([0xd6, v])  # zoom on/off
            self.command([0xa7 - v])  # inverted display
            zoom = v
    
    def draw_screen(self,):
        self.set_zoom(1)
        self.set_pos()
        i2c.write(OLED_ADDRESS, screen)
    
    def add_text(self,x, y, text, draw=1):
        global ind
        for i in range(0, min(len(text), 12 - x)):
            for c in range(0, 5):
                col = 0
                for r in range(1, 6):
                    p = Image(text[i]).get_pixel(c, r - 1)
                    col = col | (1 << r) if (p != 0) else col
                ind = x * 10 + y * 128 + i * 10 + c * 2 + 1
                screen[ind], screen[ind + 1] = col, col
        if draw == 1:
            self.set_zoom(1)
            self.set_pos(x * 5, y)
            ind0 = x * 10 + y * 128 + 1
            i2c.write(OLED_ADDRESS, b'\x40' + screen[ind0:ind + 1])

##########Motor Driver Library##########
class motordriver:
    #angle must be between 0 and 180
    def servo(self,servo_number, angle):
        buffer[0] = 0x26
        buffer[1] = servo_number + 2
        buffer[2] = 0
        buffer[3] = angle
        buffer[4] = buffer[1] ^ buffer[2] ^ buffer[3]
        i2c.write(MOTOR_DRIVER_ADDRESS, buffer)
    
    #speed must be between 0 and 255
    #direction must be 0 or 1. 0 is forward, 1 is backward
    def dc(self,dc_motor_number, speed, direction):
        buffer[0] = 0x26
        buffer[1] = dc_motor_number
        buffer[2] = speed
        buffer[3] = direction
        buffer[4] = buffer[1] ^ buffer[2] ^ buffer[3]
        i2c.write(MOTOR_DRIVER_ADDRESS, buffer)

##########SHTC3 Library##########
class SHTC3:
    def temperature(self):
        val[0] = 0x7C
        val[1] = 0xA2
        i2c.write(SHTC_ADDRESS, val)
        sleep(100)
        data = i2c.read(SHTC_ADDRESS, 6)
        temperature = ((data[0] << 8) | data[1]) * 175 / 65535 - 45
        return temperature
    
    def humidity(self):
        val[0] = 0x7C
        val[1] = 0xA2
        i2c.write(SHTC_ADDRESS, val)
        sleep(100)
        data = i2c.read(SHTC_ADDRESS, 6)
        humidty = ((data[3] << 8) | data[4]) * 100 / 65535
        return humidty

##########IR Library##########
class IRM:
    def __init__(self):
        self.KEY=-1
        self.timer=-1
    def get(self,pin):
        self.bit = []
        self.bit_t = []
        t = machine.time_pulse_us(pin, 1)
        if(4000<t<5000):
            while (len(self.bit_t)<32):
                t = machine.time_pulse_us(pin, 1)
                self.bit_t.append(t)
            for _tus in self.bit_t:self.bit.append(1 if _tus > 1000 else 0)
            output_verify = 0
            seed = 1
            for x in  self.bit[0:14]:
                if(x == 1):
                    output_verify = output_verify + seed
                seed = seed * 2
            if(output_verify!=16128): return -1
            output_key = 0
            seed = 1
            for x in  self.bit[16:23]:
                if(x == 1):
                    output_key = output_key + seed
                seed = seed * 2
            if(output_verify==16128):
                self.KEY = output_key
                self.timer = 0
                return output_key
        elif(2000<t<3000):
            self.timer=self.timer+1
            if(self.timer>2):
                self.timer=0
                return self.KEY     
        return -1

##########APDS9960 Library##########
class APDS9960:
    def init_color_sensor(self):
        val[0] = 0x81
        val[1] = 0xFC
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0x8F
        val[1] = 0x03
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0x80
        val[1] = 0x00
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0xAB
        val[1] = 0x00
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0xE7
        val[1] = 0x00
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0x80
        val[1] = 0x03
        i2c.write(APDS9960_ADDRESS, val)
    
    def read_color(self):
        buf[0] = 0x93
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        if(data == b'\x11'):
            #Red Values
            buf[0] = 0x96
            i2c.write(APDS9960_ADDRESS, buf)
            RDATAL = i2c.read(APDS9960_ADDRESS, 1)
            buf[0] = 0x97
            i2c.write(APDS9960_ADDRESS, buf)
            RDATAH = i2c.read(APDS9960_ADDRESS, 1)
            #Green Values
            buf[0] = 0x98
            i2c.write(APDS9960_ADDRESS, buf)
            GDATAL = i2c.read(APDS9960_ADDRESS, 1)
            buf[0] = 0x99
            i2c.write(APDS9960_ADDRESS, buf)
            GDATAH = i2c.read(APDS9960_ADDRESS, 1)
            #Blue Values
            buf[0] = 0x9A
            i2c.write(APDS9960_ADDRESS, buf)
            BDATAL = i2c.read(APDS9960_ADDRESS, 1)
            buf[0] = 0x9B
            i2c.write(APDS9960_ADDRESS, buf)
            BDATAH = i2c.read(APDS9960_ADDRESS, 1)
            #Calculate
            red = RDATAL + RDATAH * 256
            green = GDATAL + GDATAH * 256
            blue = BDATAL + BDATAH * 256
    
            if (red > green) and (red > blue):
                return "red"
            if (green > red) and (green > blue):
                return "green"
            if (blue > red) and (blue > green):
                return "blue"

    def color_value(self, color):
        buf[0] = 0x93
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        if(data == b'\x11'):
            #Red Values
            buf[0] = 0x96
            i2c.write(APDS9960_ADDRESS, buf)
            RDATAL = i2c.read(APDS9960_ADDRESS, 1)
            buf[0] = 0x97
            i2c.write(APDS9960_ADDRESS, buf)
            RDATAH = i2c.read(APDS9960_ADDRESS, 1)
            #Green Values
            buf[0] = 0x98
            i2c.write(APDS9960_ADDRESS, buf)
            GDATAL = i2c.read(APDS9960_ADDRESS, 1)
            buf[0] = 0x99
            i2c.write(APDS9960_ADDRESS, buf)
            GDATAH = i2c.read(APDS9960_ADDRESS, 1)
            #Blue Values
            buf[0] = 0x9A
            i2c.write(APDS9960_ADDRESS, buf)
            BDATAL = i2c.read(APDS9960_ADDRESS, 1)
            buf[0] = 0x9B
            i2c.write(APDS9960_ADDRESS, buf)
            BDATAH = i2c.read(APDS9960_ADDRESS, 1)
            #Calculate
            red = RDATAL + RDATAH * 256
            green = GDATAL + GDATAH * 256
            blue = BDATAL + BDATAH * 256
    
            if (color == "red"):
                return red
            if (color == "green"):
                return green
            if (color == "blue"):
                return blue
    
    def init_gesture_sensor(self):
        val[0] = 0x81
        val[1] = 0xFC
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0x8F
        val[1] = 0x03
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0x80
        val[1] = 0x00
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0xAB
        val[1] = 0x00
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0xE7
        val[1] = 0x00
        i2c.write(APDS9960_ADDRESS, val)
        buf[0] = 0x92
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        val[0] = 0x83
        val[1] = 0xFF
        i2c.write(APDS9960_ADDRESS, val)
        val[0] = 0x8E
        val[1] = 0x89
        i2c.write(APDS9960_ADDRESS, val)
        buf[0] = 0x90
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        val[0] = 0x90
        val[1] = 0x31
        i2c.write(APDS9960_ADDRESS, val)
        buf[0] = 0xAB
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        val[0] = 0xAB
        val[1] = 0x00
        i2c.write(APDS9960_ADDRESS, val)
        buf[0] = 0xAB
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        val[0] = 0xAB
        val[1] = 0x01
        i2c.write(APDS9960_ADDRESS, val)
        buf[0] = 0x80
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        val[0] = 0x80
        val[1] = 0x01
        i2c.write(APDS9960_ADDRESS, val)
        buf[0] = 0x80
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        val[0] = 0x80
        val[1] = 0x09
        i2c.write(APDS9960_ADDRESS, val)
        buf[0] = 0x80
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        val[0] = 0x80
        val[1] = 0x0D
        i2c.write(APDS9960_ADDRESS, val)
        buf[0] = 0x80
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        val[0] = 0x80
        val[1] = 0x4D
        i2c.write(APDS9960_ADDRESS, val)
    
    def read_gesture(self):   
        buf[0] = 0xAF 
        i2c.write(APDS9960_ADDRESS, buf)
        data = i2c.read(APDS9960_ADDRESS, 1)
        buf[0] = 0x80  
        i2c.write(APDS9960_ADDRESS, buf)
        data2 = i2c.read(APDS9960_ADDRESS, 1)
        if(data == 0) or (data2 == 0):
            return
    
        sleep(30)
        buf[0] = 0xAF  #Available
        i2c.write(APDS9960_ADDRESS, buf)
        gstatus = i2c.read(APDS9960_ADDRESS, 1)
        buf[0] = 0xAE  #fifo_level
        i2c.write(APDS9960_ADDRESS, buf)
        fifo_level = i2c.read(APDS9960_ADDRESS, 1)
        if(gstatus == 0) or (fifo_level == 0):
            return
        
        for i in range(0, 32):
            buf[0] = 0xFC
            i2c.write(APDS9960_ADDRESS, buf)
            data = i2c.read(APDS9960_ADDRESS, 1)
            u_data[i] = int.from_bytes(data, "big") 
            
            buf[0] = 0xFD
            i2c.write(APDS9960_ADDRESS, buf)
            data = i2c.read(APDS9960_ADDRESS, 1)
            d_data[i] = int.from_bytes(data, "big") 
            
            buf[0] = 0xFE
            i2c.write(APDS9960_ADDRESS, buf)
            data = i2c.read(APDS9960_ADDRESS, 1)
            l_data[i] = int.from_bytes(data, "big") 
            
            buf[0] = 0xFF
            i2c.write(APDS9960_ADDRESS, buf)
            data = i2c.read(APDS9960_ADDRESS, 1)
            r_data[i] = int.from_bytes(data, "big") 
            sleep(10)
    
        u_first = 0
        d_first = 0
        l_first = 0
        r_first = 0
        u_last = 0
        d_last = 0
        l_last = 0
        r_last = 0
    
        for i in range(0, 32):
            if u_data[i] > APDS9960_GESTURE_THRESHOLD_OUT and \
                d_data[i] > APDS9960_GESTURE_THRESHOLD_OUT and \
                l_data[i] > APDS9960_GESTURE_THRESHOLD_OUT and \
                r_data[i] > APDS9960_GESTURE_THRESHOLD_OUT:
    
                u_first = u_data[i]
                d_first = d_data[i]
                l_first = l_data[i]
                r_first = r_data[i]
                break
    
        if u_first == 0 or  d_first == 0 or l_first == 0 or r_first == 0:
            return 
    
        for i in reversed(range(0, 32)):
            if u_data[i] > APDS9960_GESTURE_THRESHOLD_OUT and \
                d_data[i] > APDS9960_GESTURE_THRESHOLD_OUT and \
                l_data[i] > APDS9960_GESTURE_THRESHOLD_OUT and \
                r_data[i] > APDS9960_GESTURE_THRESHOLD_OUT:
    
                u_last = u_data[i]
                d_last = d_data[i]
                l_last = l_data[i]
                r_last = r_data[i]
                break
    
        # calculate the first vs. last ratio of up/down and left/right
        ud_ratio_first = ((u_first - d_first) * 100) / (u_first + d_first)
        lr_ratio_first = ((l_first - r_first) * 100) / (l_first + r_first)
        ud_ratio_last = ((u_last - d_last) * 100) / (u_last + d_last)
        lr_ratio_last = ((l_last - r_last) * 100) / (l_last + r_last)
    
        # determine the difference between the first and last ratios
        ud_delta = ud_ratio_last - ud_ratio_first
        lr_delta = lr_ratio_last - lr_ratio_first
    
        gesture_ud_delta_ = 0
        gesture_lr_delta_ = 0
        
        gesture_ud_count_ = 0
        gesture_lr_count_ = 0
    
        # accumulate the UD and LR delta values
        gesture_ud_delta_ += ud_delta
        gesture_lr_delta_ += lr_delta
    
        # determine U/D gesture
        if gesture_ud_delta_ >= APDS9960_GESTURE_SENSITIVITY_1:
            gesture_ud_count_ = 1
        elif gesture_ud_delta_ <= -APDS9960_GESTURE_SENSITIVITY_1:
            gesture_ud_count_ = -1
        else:
            gesture_ud_count_ = 0
    
        if gesture_lr_delta_ >= APDS9960_GESTURE_SENSITIVITY_1:
            gesture_lr_count_ = 1
        elif gesture_lr_delta_ <= -APDS9960_GESTURE_SENSITIVITY_1:
            gesture_lr_count_ = -1;
        else:
            gesture_lr_count_ = 0;
    
        if gesture_ud_count_ == -1 and gesture_lr_count_ == 0:
            return "UP"
        elif gesture_ud_count_ == 1 and gesture_lr_count_ == 0:
            return "DOWN"
        elif gesture_ud_count_ == 0 and gesture_lr_count_ == 1:
            return "RIGHT"
        elif gesture_ud_count_ == 0 and gesture_lr_count_ == -1:
            return "LEFT"
        elif gesture_ud_count_ == -1 and gesture_lr_count_ == 1:
            if abs(gesture_ud_delta_) > abs(gesture_lr_delta_):
                return "UP"
            else:
                return "DOWN"
        elif gesture_ud_count_ == 1 and gesture_lr_count_ == -1:
            if abs(gesture_ud_delta_) > abs(gesture_lr_delta_):
                return "DOWN"
            else:
                return "LEFT"
        elif gesture_ud_count_ == -1 and gesture_lr_count_ == -1:
            if abs(gesture_ud_delta_) > abs(gesture_lr_delta_):
                return "UP"
            else:
                return "LEFT"
        elif gesture_ud_count_ == 1 and gesture_lr_count_ == 1:
            if abs(gesture_ud_delta_) > abs(gesture_lr_delta_):
                return "DOWN"
            else:
                return "RIGHT"

##########HCSR04 Library##########
def measure_distance():
    # Send a 10µs pulse to the trigger to initiate measurement
    pin2.write_digital(0)
    time.sleep_us(2)
    pin2.write_digital(1)
    time.sleep_us(10)
    pin2.write_digital(0)
    
    # Initialize start and end times
    start_time = 0
    end_time = 0
    
    # Measure the duration of the echo pulse
    while pin1.read_digital() == 0:
        start_time = time.ticks_us()
    while pin1.read_digital() == 1:
        end_time = time.ticks_us()
    
    # Calculate the distance based on the echo time
    duration = end_time - start_time
    distance_cm = (duration / 2) * 0.0343  # Speed of sound is 343 m/s (0.0343 cm/µs)
    return distance_cm
