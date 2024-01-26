from microbit import i2c

motor_driver_address = 0x22
val = bytearray(5)
val[0] = 0x26

#angle must be between 0 and 90
def servomotor(servo_number, angle):
    if(servo_number == 1):
        val[1] = 0x03
    elif(servo_number == 2):
        val[1] = 0x04
    elif(servo_number == 3):
        val[1] = 0x05
    else:
        val[1] = 0x06
    val[2] = 0x00
    val[3] = angle
    val[4] = val[1] ^ angle
    i2c.write(motor_driver_address, val)

#speed must be between 0 and 255
#direction must be 0 or 1. 0 is forward, 1 is backward
def dcmotor(dc_motor_number, speed, direction):
    val[1] = dc_motor_number
    val[2] = speed
    val[3] = direction
    val[4] = dc_motor_number ^ speed ^ direction
    i2c.write(motor_driver_address, val)

    
    
