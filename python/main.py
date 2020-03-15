import sensors as s
import comunication as c

def justGo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(20, GPIO.LOW)


def autopilot():
    c.waitForConnection()
    c.getRoute(s.getGPS())

if __name__ == '__main__':
    try:
        '''while True:
            dist = s.distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)'''


        s.setup()
        #autopilot()
        s.beep()
        justGo()

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
