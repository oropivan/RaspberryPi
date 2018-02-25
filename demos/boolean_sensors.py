#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# GPIO setup
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    print("FIRE!!!!")

# Detect both HIGH & LOW
# Ignore events for 300 ms
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) 

GPIO.add_event_callback(channel, callback)

# demo
while True:
    # conserve CPU resources.
    time.sleep(1)

