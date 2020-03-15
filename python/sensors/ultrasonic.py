import time
import RPi.GPIO as GPIO

class Ultrasonic:
    def __init__(self, pinTrigger, pinEcho):
        self.pinTrigger = pinTrigger
        self.pinEcho = pinEcho
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinTrigger, GPIO.OUT)
        GPIO.setup(pinEcho, GPIO.IN)

    def read(self):
        # set Trigger to HIGH
        GPIO.output(self.pinTrigger, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.pinTrigger, False)

        start = time.time()

        while GPIO.input(self.pinEcho)==0:    #Wait for the echo to go high- starting the measurement.
            pass

        start = time.time()

        while GPIO.input(self.pinEcho)==1:    #Wait for the echo to go low
            pass

        stop = time.time()

        # time difference between start and arrival
        TimeElapsed = stop - start
        # sonic speed in air(34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        return distance
