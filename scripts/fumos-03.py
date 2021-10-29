import RPi.GPIO as GPIO
import time
import board
import neopixel
from datetime import datetime 

iSensorPin = 7 # GPIO4
iSensorPin = 4 # GPIO4 - board.D7 
iRelayPin = 23 # GPIO23 - board.D16
iteration = 0

# neopixel pin
iNeopixelPin = board.D18

# The number of NeoPixels
num_pixels = 5

# setup pixel array
pixels = neopixel.NeoPixel(iNeopixelPin, num_pixels)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def clear_pixels(r,g,b):
     for i in range(num_pixels):
          pixels[i] = (r,g,b)
     pixels.show()



GPIO.setmode(GPIO.BCM)
print("board.D7",board.D7,type(board.D7))
print("iSensorPin",iSensorPin, type(iSensorPin) )
time.sleep(2)
GPIO.setup(iSensorPin, GPIO.IN)
GPIO.setup(iRelayPin, GPIO.OUT)

GPIO.output(iRelayPin, False)

def MotionDetected(iSensorPin):
    print( datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "-> Motion Detected!")
    GPIO.output(iRelayPin, True)
    time.sleep(5)
    GPIO.output(iRelayPin, False)

    clear_pixels(150, 0, 0)
    time.sleep(2)
    clear_pixels(0, 0, 0)
    time.sleep(10)



# MAIN 
time.sleep(2)
print(iteration, "-> Ready!")
clear_pixels(0,0,0)
while True:
  try:
#    GPIO.add_event_detect(iSensorPin, GPIO.RISING, callback=MotionDetected)
    if GPIO.input(iSensorPin):
      print("GPIO input", GPIO.input(iSensorPin))
      time.sleep(2)
    while 1:
        pass
  except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()

