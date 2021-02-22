import RPi.GPIO as GPIO
from time import sleep

def Motor3():
    GPIO.setmode(GPIO.BOARD)
    m1b = 33
    m2b = 31
    m3b = 29
    
    GPIO.setup(m1b,GPIO.OUT)
    GPIO.setup(m2b,GPIO.OUT)
    GPIO.setup(m3b,GPIO.OUT)

    if(GPIO.input(11)== True):
        print("Forward")
        GPIO.output(m1b,GPIO.HIGH)
        GPIO.output(m2b,GPIO.LOW)
        GPIO.output(m3b,GPIO.HIGH)
        sleep(3)
        print("Rückwets")
        GPIO.output(m2b,GPIO.HIGH)
        GPIO.output(m3b,GPIO.LOW)
        sleep(3)
        GPIO.output(m3b,GPIO.LOW)
        GPIO.cleanup()
