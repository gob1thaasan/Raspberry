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
GPIO.setup(8,GPIO.OUT) # input 3.3v from volt pin 8
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) # push button using pin 11

GPIO.output(8,False)

def myblink()
    GPIO.output(8,True)
    time.sleep(0.5)
    GPIO.output(8,False)
    time.sleep(0.5)
    return;

print("Coding running! Press CTRL+C to exit") #break while loop when CTL+C is pressed

try:
    while True:
        # When button is pressed, turn the LED ON
        if GPIO.input(11):
            print("Pin 11 is HIGH")
            GPIO.output(8,True)
        # When button is NOT pressed, blink the LED
        else:
            print("Pin 11 is LOW")
            myblink()
            
except KeyboardInterrupt: # If CTRL+C is pressed, break the loop.
    GPIO.cleanup() # cleanup all GPIO pins


