import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
#iSensorPin = 4 # GPIO4 - board.D7
GPIO.setup(PIR_PIN, GPIO.IN)
#print(“PIR”)
time.sleep(2)
print('Ready')
while True:
      if GPIO.input(PIR_PIN):
         print('Motion Detected!')
      print(GPIO.input(PIR_PIN)) 
      time.sleep(1)

