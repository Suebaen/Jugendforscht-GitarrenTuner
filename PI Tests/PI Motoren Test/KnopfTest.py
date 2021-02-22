import RPi.GPIO as GPIO
from time import sleep
from  ZweiMotoren import *
from Motor1 import *
from Motor2 import *
from Motor3 import *

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BOARD)

print("Hallo")
while (True):
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    if(GPIO.input(11)== True):
            sleep (0.1)
            print("Knopf 1\n")
            test()
            
    else:
        GPIO.cleanup

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    if(GPIO.input(13)== True):
            sleep (0.1)
            print("Knopf 2\n")
    else:
        GPIO.cleanup

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    if(GPIO.input(15)== True):
            sleep (0.1)
            print("Knopf 3\n")
    else:
        GPIO.cleanup


