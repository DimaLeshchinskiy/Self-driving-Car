import time
import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pinIN1, pinIN2):
        self.pinIN1 = pinIN1
        self.pinIN2 = pinIN2
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pinIN1, GPIO.OUT)
        GPIO.setup(pinIN2, GPIO.OUT)

    def forward(self):
        GPIO.output(self.pinIN1, GPIO.HIGH)
        GPIO.output(self.pinIN2, GPIO.LOW)

    def backward(self):
        GPIO.output(self.pinIN1, GPIO.LOW)
        GPIO.output(self.pinIN2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pinIN1, GPIO.LOW)
        GPIO.output(self.pinIN2, GPIO.LOW)
