import RPi.GPIO as GPIO
from subprocess import call
from  time import sleep
from NurDasA import *
from NurDasC import *
from NurDasD import *
from NurDasE import *
from NurDasF import *
from NurDasG import *
from test2 import *
import _portaudio as pa





GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BOARD)

        


while (True):

#Kopf1    
    if(GPIO.input(11)== True):
        sleep (0.1)
        print("Knopf 1\n")
        print("Willst du ein A(Button1) oder ein D (Button2)Stimmen?\n")
        TonA()
        # if (GPIO.input(11)== True):
        #     print("Jetzt wird das A gestimmt")
        #     TonA()
        # if (GPIO.input(15)==True):
        #     print("Jetzt wird das D gestimmt")
        #     TonD()  
        
        # super()

    else:
        GPIO.cleanup

#Kopf2
    if(GPIO.input(15)== True):
        sleep (0.1)
        print("Knopf 2\n")
        print("Willst du ein C (Button1) oder ein E (Button2)Stimmen?\n")
        TonC()
        # if (GPIO.input(11)== True):
        #     print("Jetzt wird das C gestimmt")
        #     TonC()
        # if (GPIO.input(15)==True):
        #     print("Jetzt wird das E gestimmt")
        #     TonE()

#Kopf3        
    else:
        GPIO.cleanup
    
    if(GPIO.input(13)== True):
        sleep (0.1)
        print("Knopf 3\n")
        print("Willst du ein F(Button1) oder ein G (Button2)Stimmen?\n")
        TonD()
        # if (GPIO.input(11)== True):
        #     print("Jetzt wird das F gestimmt")
        #     TonF()
        # if (GPIO.input(15)==True):
        #     print("Jetzt wird das G gestimmt")
        #     TonG()
        
  
    else:
        GPIO.cleanup