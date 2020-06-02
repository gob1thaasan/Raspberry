'''
first blink program

'''

import RPi.GPIO as GPIO
import time #using time function for blink
import os

os.system('clear') #clear terminal
print('hello world') #echo

GPIO.setmode(GPIO.BOARD) # using gpio onboard numbering system
GPIO.setup(8,GPIO.OUT) #using gnd pin 6 and input volt pin 8

print("Here we go! Press CTRL+C to exit")
try:
    while True:
        GPIO.output(8,True)
        time.sleep(0.5)
        GPIO.output(8,False)
        time.sleep(0.5)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO