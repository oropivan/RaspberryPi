#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

RelayPin1 = 18
RelayPin2 = 17
RelayPin3 = 15
RelayPin4 = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(RelayPin1, GPIO.OUT)
GPIO.setup(RelayPin2, GPIO.OUT)
GPIO.setup(RelayPin3, GPIO.OUT)
GPIO.setup(RelayPin4, GPIO.OUT)

GPIO.output(RelayPin1, GPIO.HIGH)
GPIO.output(RelayPin2, GPIO.HIGH)
GPIO.output(RelayPin3, GPIO.HIGH)
GPIO.output(RelayPin4, GPIO.HIGH)


Relays = [RelayPin1, RelayPin2, RelayPin3, RelayPin4]

def loop():
    while True:
        print '...close'
        for i in range(0,4):
            GPIO.output(Relays[i], GPIO.LOW)
            time.sleep(1)
        print 'open...'
        for i in range(0,4):
            GPIO.output(Relays[i], GPIO.HIGH)
            time.sleep(1)
        time.sleep(0.5)

def destroy():
  GPIO.output(RelayPin1, GPIO.HIGH)
  GPIO.cleanup()

if __name__ == '__main__':
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()


                                                                                                                    
