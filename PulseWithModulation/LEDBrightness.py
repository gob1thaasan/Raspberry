'''
Using Pulse With Modulation to control the brightness of the light.
Gobithaasan 11/6/2020
'''
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT) # on  board is 32, ground is 30

pwm = GPIO.PWM(32,100) # (output pin, frequency of PWM signal) 
pwm.start(0) # start with 0% duty cycle; LED will be on for 0%

try:
   while True:
      for i in range(50): # duty cycle increment from 0-50
        print(i) # keep track of increment on terminal
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)

      for i in range(50,0,-1):  # decrement from 50-0
        print(i)
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)
      os.system('clear')
      print('New round!')

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	os.system('clear')	
	print('Bye!')	
	pwm.stop()
	GPIO.cleanup
