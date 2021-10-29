import RPi.GPIO as GPIO
from datetime import datetime, date, time, timezone
import time

sensorPin = 3     # GPIO 2
transistorPin = 7     # GPIO 4
shortDelay = 1   # 1s
loopDelay = 1.5   # 1s
longDelay = 3   # 5s
LoopCnt = 100

#def main():
    #for i in range(LoopCnt):
        #GPIO.output(transistorPin, GPIO.HIGH)  # output 3.3 V from GPIO pin
        #time.sleep(longDelay)   # delay for 1s
        #GPIO.output(transistorPin , GPIO.LOW)  # output 0 V from GPIO pin
        #time.sleep(shortDelay)   # delay for 1s
 

def main():
    n=0
    while True:
         i=GPIO.input(sensorPin)
         n=n+3
         if i==0: #When output from motion sensor is LOW
              print (n,"no intruders",i)
              GPIO.output(transistorPin,0) #Turn off fumos
              time.sleep(loopDelay)
         elif i==1: #When output from motion sensor is HIGH
              print (n,"Intruder detected",i)
              GPIO.output(transistorPin,1) #Turn ON fumos
              time.sleep(loopDelay)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup()  # free up the resources used
    GPIO.setup(transistorPin, GPIO.OUT)    # initialize GPIO pin as OUTPUT pin
    GPIO.output(transistorPin, GPIO.LOW)
    GPIO.setup(sensorPin, GPIO.IN)

if __name__ == '__main__':
    setup()
    main()
    GPIO.cleanup()  # free up the resources used
