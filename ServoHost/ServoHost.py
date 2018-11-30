#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import threading
from flask import Flask

#NOTE these are for the light function
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(16, GPIO.OUT)

app = Flask(__name__)
listenPort = 8614
hostIp = "192.168.0.20"
print("Listening...")

def getDuty(angle):
    return float(angle) / 10.0 + 2.5

@app.route("/light", methods=["POST"])
def light():
    for i in range (5):
        GPIO.output(16,True)
        time.sleep(1)
        GPIO.output(16, False)
        time.sleep(3)
    return "Method \"light\" not implemented"

@app.route("/flush", methods=["POST"])
def flush():
#    flushReady = threading.Event()

    flushThread = threading.Thread(target=flushing)
    flushThread.start()
    return "Flushed The Toilet"


def flushing():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18,100)

    duty = getDuty(180)

    print(duty)
    pwm.ChangeDutyCycle(duty)
    pwm.start(duty)
    time.sleep(2)
    pwm.stop()

    duty = getDuty(0)

    print(duty)
    pwm.ChangeDutyCycle(duty)
    pwm.start(duty)
    time.sleep(2)
    pwm.stop()
    GPIO.cleanup()

    return "Flushed the toilet!"

if __name__ == "__main__":
    #setup pwm on io
    GPIO.cleanup()    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 100)

    #reset servo to 0
    pwm.start(getDuty(0))
    time.sleep(1)
    pwm.stop()

    GPIO.cleanup()

    #init webHost
    app.run(host = hostIp, port = listenPort)

    #cleanup on shutdown
    print("Cleanup")
    GPIO.cleanup()
