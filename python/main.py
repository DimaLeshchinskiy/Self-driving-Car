import sensors as s
import comunication as c

def justGo():
    s.test()


def autopilot():
    c.waitForConnection()
    c.getRoute(s.getGPS())

if __name__ == '__main__':
    try:
        #autopilot()
        justGo()

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
