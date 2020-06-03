'''
A circuit using aspberry Pi 4B that causes an LED to blink when a push button is NOT pressed. However, the LED stay on continually when the push button IS pressed.

Gobithaasan 3/6/2020
'''

import RPi.GPIO as GPIO
import time #using time function for blink
import os

os.system('clear') #clear terminal
print('hello world') #echo

GPIO.setmode(GPIO.BOARD) # using gpio onboard numbering system
GPIO.setup(8,GPIO.OUT) #using gnd pin 6 and input volt pin 8
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)


print("Coding running! Press CTRL+C to exit")
try:
    while True:
    
        if GPIO.input(11):
            print("Pin 11 is HIGH")
            GPIO.output(8,True)
        else:
        print("Pin 11 is LOW")
            GPIO.output(8,True)
            time.sleep(0.5)
            GPIO.output(8,False)
            time.sleep(0.5)
            
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
