#!usr/bin/python
import RPi.GPIO as GPIO
import time

IN1 = 17 # BCM
IN2 = 27
IN3 = 22
IN4 = 18

def setStep(in1, in2, in3, in4):
    GPIO.output(IN1, in1)
    GPIO.output(IN2, in2)
    GPIO.output(IN3, in3)
    GPIO.output(IN4, in4)

def stop():
    setStep(0,0,0,0)

def forward_wave(delay, steps):
    for i in range(0, steps):
        setStep(1,0,0,0)
        time.sleep(delay)
        setStep(0,1,0,0)
        time.sleep(delay)
        setStep(0,0,1,0)
        time.sleep(delay)
        setStep(0,0,0,1)
        time.sleep(delay)

def backward_wave(delay, steps):
    for i in range(0, steps):
        setStep(0,0,0,1)
        time.sleep(delay)
        setStep(0,0,1,0)
        time.sleep(delay)
        setStep(0,1,0,0)
        time.sleep(delay)
        setStep(1,0,0,0)
        time.sleep(delay)

def forward_fullstep(delay, steps):
    for i in range(0,steps):
        setStep(1,1,0,0)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(0,0,1,1)
        time.sleep(delay)
        setStep(1,0,0,1)
        time.sleep(delay)
        
def backward_fullstep(delay, steps):
    for i in range(0,steps):
        setStep(1,0,0,1)
        time.sleep(delay)
        setStep(0,0,1,1)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(1,1,0,0)
        time.sleep(delay)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def start():
    while True:
        print "FORWARD"
        forward_wave(0.03, 512)
        stop()
        print "FULL STEP"
        forward_fullstep(0.03, 512)
        stop()

        print "BACKWARD"
        backward_wave(0.05, 512)
        stop()
        print "FULL STEP"
        backward_fullstep(0.05, 512)
        stop()

        time.sleep(2)
def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print "Warm up your motors"
    setup()
    try:
        start()
    except KeyboardInterrupt:
        print "Cleaning your mess"
        destroy()

