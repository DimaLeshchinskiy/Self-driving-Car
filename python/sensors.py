#Libraries
import RPi.GPIO as GPIO
import time

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

ForwardLeft = 20
BackwardLeft = 16
ForwardRight = 26
BackwardRight = 19

buzzer = 17

def setup():
    global GPIO_TRIGGER, GPIO_ECHO
    global ForwardLeft, BackwardLeft, ForwardRight, BackwardRight
    global buzzer
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    #set GPIO direction (IN / OUT)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    GPIO.setup(ForwardLeft, GPIO.OUT)
    GPIO.setup(BackwardLeft, GPIO.OUT)
    GPIO.setup(ForwardRight, GPIO.OUT)
    GPIO.setup(BackwardRight, GPIO.OUT)

    GPIO.setup(buzzer, GPIO.OUT)



def distance():
    global GPIO_TRIGGER, GPIO_ECHO
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:    #Wait for the echo to go high- starting the measurement.
        pass

    start = time.time()

    while GPIO.input(GPIO_ECHO)==1:    #Wait for the echo to go low
        pass

    stop = time.time()

    # time difference between start and arrival
    TimeElapsed = stop - start
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance

def getGPS():
    pass

def beep(sec=1):
    global buzzer
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(sec)
    GPIO.output(buzzer, GPIO.HIGH)

def moveForward():
    global ForwardLeft, BackwardLeft, ForwardRight, BackwardRight
    GPIO.output(ForwardLeft, GPIO.HIGH)
    GPIO.output(ForwardRight, GPIO.HIGH)
    GPIO.output(BackwardLeft, GPIO.LOW)
    GPIO.output(BackwardRight, GPIO.LOW)

def moveLeft():
    global ForwardLeft, BackwardLeft, ForwardRight, BackwardRight
    GPIO.output(ForwardLeft, GPIO.LOW)
    GPIO.output(ForwardRight, GPIO.HIGH)
    GPIO.output(BackwardLeft, GPIO.HIGH)
    GPIO.output(BackwardRight, GPIO.LOW)

def moveRight():
    global ForwardLeft, BackwardLeft, ForwardRight, BackwardRight
    GPIO.output(ForwardLeft, GPIO.HIGH)
    GPIO.output(ForwardRight, GPIO.LOW)
    GPIO.output(BackwardLeft, GPIO.LOW)
    GPIO.output(BackwardRight, GPIO.HIGH)

def moveBack():
    global ForwardLeft, BackwardLeft, ForwardRight, BackwardRight
    GPIO.output(ForwardLeft, GPIO.LOW)
    GPIO.output(ForwardRight, GPIO.LOW)
    GPIO.output(BackwardLeft, GPIO.HIGH)
    GPIO.output(BackwardRight, GPIO.HIGH)

def moveStop():
    global ForwardLeft, BackwardLeft, ForwardRight, BackwardRight
    GPIO.output(ForwardLeft, GPIO.LOW)
    GPIO.output(ForwardRight, GPIO.LOW)
    GPIO.output(BackwardLeft, GPIO.LOW)
    GPIO.output(BackwardRight, GPIO.LOW)

def moveDemo():
    print("Forward")
    moveForward()
    time.sleep(5)
    print("Back")
    moveBack()
    time.sleep(5)
    print("Left")
    moveLeft()
    time.sleep(5)
    print("Right")
    moveRight()
    time.sleep(5)
    print("Stop")
    moveStop()
