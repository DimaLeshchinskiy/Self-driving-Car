import time
import RPi.GPIO as GPIO

class Buzzer:
    def __init__(self, pinIn):
        self.pinIn = pinIn
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinIn, GPIO.OUT)

    def beep(self, sec=1):
        GPIO.output(self.pinIn, GPIO.LOW)
        time.sleep(sec)
        GPIO.output(self.pinIn, GPIO.HIGH)
