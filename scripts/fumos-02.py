import RPi.GPIO as GPIO
import time
from datetime import datetime 

iSensorPin = 7
iLedPin = 16
iteration = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(iSensorPin, GPIO.IN)
GPIO.setup(iLedPin, GPIO.OUT)

GPIO.output(iLedPin, False)

def MotionDetected(iSensorPin):
    print( datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "-> Motion Detected!")
    GPIO.output(iLedPin, True)
    time.sleep(5)
    GPIO.output(iLedPin, False)

time.sleep(2)
print(iteration, "-> Ready!")

try:
    GPIO.add_event_detect(iSensorPin, GPIO.RISING, callback=MotionDetected)
    while 1:
        pass
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()

