import RPi.GPIO as GPIO
import time
import board
import neopixel
from datetime import datetime

iSensorPin = 4
#iSensorPin = 4 # GPIO4 - board.D7

# neopixel pin
#iNeopixelPin = 24 # board.D18 
iNeopixelPin = board.D18 

# The number of NeoPixels
num_pixels = 30

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
#print(“PIR”)
time.sleep(2)
print('Ready')
inc = 0
while True:
      if GPIO.input(iSensorPin):
         print(inc,'-> Motion Detected!')
         inc =+ 1
         clear_pixels(150,150,150)
      else:
         clear_pixels(0,0,0)
      #print(GPIO.input(iSensorPin)) 
      time.sleep(2)

