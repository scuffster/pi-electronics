import RPi.GPIO as GPIO
import time
import board
import neopixel
from datetime import datetime

iRelayPin = 23
#iRelayPin = 23 # GPIO23 - board.D16
iStrobePin = 25
#iStrobePin = 25 # GPIO25 - board.D22
iSensorPin = 4
#iSensorPin = 4 # GPIO4 - board.D7

# neopixel pin
#iNeopixelPin = 24 # board.D18 
iNeopixelPin = board.D18 

# The number of NeoPixels
num_pixels = 50

# setup pixel array
print("iNeoPixelsPin",type(iNeopixelPin), "num pixels",type(num_pixels))
time.sleep(1)
pixels = neopixel.NeoPixel(iNeopixelPin, num_pixels)


def clear_pixels(r,g,b):
     for i in range(num_pixels):
          pixels[i] = (r,g,b)
     pixels.show()


GPIO.setmode(GPIO.BCM)
GPIO.setup(iSensorPin, GPIO.IN)
GPIO.setup(iRelayPin, GPIO.OUT)
GPIO.setup(iStrobePin, GPIO.OUT)
#print(“PIR”)
time.sleep(2)
print('Ready')
inc = 0
clear_pixels(0,0,0)
while True:
      if GPIO.input(iSensorPin):
         inc =+ 1
         print(inc,'-> Motion Detected!')
         GPIO.output(iRelayPin, True)
         GPIO.output(iStrobePin, True)
         time.sleep(5)
         clear_pixels(150,150,150)
      else:
         clear_pixels(0,0,0)
         GPIO.output(iRelayPin, False)
         GPIO.output(iStrobePin, False)
      #print(GPIO.input(iSensorPin)) 
      time.sleep(2)

