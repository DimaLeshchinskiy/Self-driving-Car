from sensors.buzzer import Buzzer
from sensors.motors import Motors
from sensors.ultrasonic import Ultrasonic
from sensors.compass import Compass

#settings
GPIO_TRIGGER = 23
GPIO_ECHO = 24

ForwardLeft = 20
BackwardLeft = 16
ForwardRight = 26
BackwardRight = 19

buzzer = 17

def test():
    buzzer = Buzzer(buzzer)
    motors = Motors(ForwardLeft, BackwardLeft, ForwardRight, BackwardRight)
    ultrasonic = Ultrasonic(GPIO_TRIGGER, GPIO_ECHO)
    compass = Compass()

    buzzer.beep()
    motors.forward()
    motors.stop()
    distance = ultrasonic.read()
    print(distance)
    degrees = compass.read()
    print(degrees)
