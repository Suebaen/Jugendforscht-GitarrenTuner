import RPi.GPIO as GPIO
from time import sleep
from Motor1 import *
from Motor2 import *
from Motor3 import *

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BOARD)

while(True):
   
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    if(GPIO.input(11)== True):
        print("Knopf 1")
        Motor1()
    else:
        GPIO.cleanup

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    if(GPIO.input(13)== True):
        print("Knopf 2")
        Motor2()
    
    else:
        GPIO.cleanup

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    if(GPIO.input(15)== True):
        print("Knopf 3")
        Motor3()
    
    else:
        GPIO.cleanup