import RPi.GPIO as GPIO
from subprocess import call
from  time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.OUT)
        
# class CallPy(object):
#     def __init__(self,path = '/Volumes/voyager-afp/benjamin/Jufo/PI Tests/test2.py'):
#         self.path =path
    
#     def  call_python_file(self):
#         call(["Python3", "{}".format(self.path)])

while (True):
    if(GPIO.input(11)== True):
        # GPIO.output(13, True)
        sleep (0.1)
        print("Hello")
        # c= CallPy()
        # c.call_python_file() das muss immer rausgelöschtwerden aber ich weis noch nicht warum        


    else:
        GPIO.output (13,False)
        GPIO.cleanup




