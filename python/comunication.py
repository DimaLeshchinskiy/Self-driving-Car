import requests
import time

def waitForConnection():
    while True:
        url = 'https://www.w3schools.com/python/demopage.php'
        x = requests.post(url)
        if x.text == "OK":
            return
        time.sleep(1)

def getRoute(gps):
    pass
    #using TOMTOM https://developer.tomtom.com/routing-api/routing-api-documentation-routing/calculate-route
