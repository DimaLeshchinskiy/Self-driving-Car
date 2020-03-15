import time
import RPi.GPIO as GPIO
from motor import Motor

class Motors:
    def __init__(self, pinIN1, pinIN2, pinIN3, pinIN4):
        self.motorLeft = Motor(pinIN1, pinIN2)
        self.motorRight = Motor(pinIN3, pinIN4)

    def forward(self):
        self.motorLeft.forward()
        self.motorRight.forward()

    def backward(self):
        self.motorLeft.backward()
        self.motorRight.backward()

    def left(self):
        self.motorLeft.backward()
        self.motorRight.forward()

    def right(self):
        self.motorLeft.forward()
        self.motorRight.backward()

    def stop(self):
        self.motorLeft.stop()
        self.motorRight.stop()
