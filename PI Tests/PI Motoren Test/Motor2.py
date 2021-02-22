import RPi.GPIO as GPIO
from time import sleep

def Motor2():
    GPIO.setmode(GPIO.BOARD)
    m1a = 23
    m2a = 21
    m3a = 19
    
    GPIO.setup(m1a,GPIO.OUT)
    GPIO.setup(m2a,GPIO.OUT)
    GPIO.setup(m3a,GPIO.OUT)

    if(GPIO.input(11)== True):
        print("Forward")
        GPIO.output(m1a,GPIO.HIGH)
        GPIO.output(m2a,GPIO.LOW)
        GPIO.output(m3a,GPIO.HIGH)
        sleep(3)
        print("Rückwets")
        GPIO.output(m2a,GPIO.HIGH)
        GPIO.output(m3a,GPIO.LOW)
        sleep(3)
        GPIO.output(m3a,GPIO.LOW)
        GPIO.cleanup()