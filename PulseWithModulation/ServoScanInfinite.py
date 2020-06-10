'''
Using Pulse With Modulation to control the direction of the servo.
'''
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT) # on  board is 32, ground is 30

pwm = GPIO.PWM(32,40) # (output pin, frequency of PWM signal) 
pwm.start(0)

try:
   while True:
      for i in range(10): # increment from 0-10
        print(i)
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)

      for i in range(10,0,-1):  # decrement form 10-0
        print(i)
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)
      os.system('clear')
      print('New round!')

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	os.system('clear')	
	print('Bye!')	
	GPIO.cleanup
