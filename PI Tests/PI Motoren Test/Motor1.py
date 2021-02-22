import RPi.GPIO as GPIO
from time import sleep

def Motor1():
    GPIO.setmode(GPIO.BOARD)

    m1 = 7
    m2 = 5
    m3 = 3

    GPIO.setup(m1,GPIO.OUT)
    GPIO.setup(m2,GPIO.OUT)
    GPIO.setup(m3,GPIO.OUT)
    if(GPIO.input(11)== True):
        print("Forward")
        GPIO.output(m1,GPIO.HIGH)
        GPIO.output(m2,GPIO.LOW)
        GPIO.output(m3,GPIO.HIGH)
        sleep(3)
        print("Rückwets")
        GPIO.output(m2,GPIO.HIGH)
        GPIO.output(m3,GPIO.LOW)
        sleep(3)
        GPIO.output(m3,GPIO.LOW)
        GPIO.cleanup()