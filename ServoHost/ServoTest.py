
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)

angle = 180

time.sleep(10)

duty = float(angle) / 10.0 + 2.5
print(angle)
print(duty)
pwm.ChangeDutyCycle(duty)

pwm.start(duty)
time.sleep(2)
pwm.stop()



#new
duty = float(0) / 10.0 + 2.5
print("0")
print(duty)
pwm.ChangeDutyCycle(duty)
pwm.start(duty)
time.sleep(1)
pwm.stop()

GPIO.cleanup()
