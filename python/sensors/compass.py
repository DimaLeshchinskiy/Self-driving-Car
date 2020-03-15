import time
import smbus

class Compass:
    def __init__(self):
        pass

    def getOrientation(self, deg):
        output = ""
        if(22.5 <= deg < 67.5):
            output = "NE "
        elif(67.5 <= deg < 112.5):
            output = "E "
        elif(112.5 <= deg < 157.5):
            output = "SE "
        elif(157.5 <= deg < 202.5):
            output = "S "
        elif(202.5 <= deg < 247.5):
            output = "SW "
        elif(247.5 <= deg < 292.5):
            output = "W "
        elif(292.5 <= deg < 337.5):
            output = "NW "
        else:
            output = "N "

        output = output + str(deg) + " degrees"
        return output

    def read(self):
        bus = smbus.SMBus(1)

        DEVICE_ADDRESS = 0x21
        DEVICE_READ_ADDRESS = 0x41

        data = bus.read_i2c_block_data(DEVICE_ADDRESS, DEVICE_READ_ADDRESS, 2)
        degrees = ((data[0] << 8) + data[1]) / 10
        return degrees
