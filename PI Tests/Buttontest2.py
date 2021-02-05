import RPi.GPIO as GPIO
from subprocess import call
from  time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BOARD)

# GPIO
        
# class CallPy(object):
#     def __init__(self,path = '/Volumes/voyager-afp/benjamin/Jufo/PI Tests/test2.py'):
#         self.path =path
    
#     def  call_python_file(self):
#         call(["Python3", "{}".format(self.path)])

while (True):
    if(GPIO.input(11)== True):
        # GPIO.output(13, True)
        sleep (0.1)
        print("Knopf 1")
        # c= CallPy()
              
    

    else:
        # GPIO.output (13,False)
        GPIO.cleanup


    if(GPIO.input(15)== True):
       # GPIO.output(13, True)
        sleep (0.1)
        print("Knopf 2")
        # c= CallPy()
              
    

    else:
        # GPIO.output (13,False)
        GPIO.cleanup
    
    if(GPIO.input(13)== True):
       # GPIO.output(13, True)
        sleep (0.1)
        print("Knopf 3")
        # c= CallPy()
              
    

    else:
        # GPIO.output (13,False)
        GPIO.cleanup
    
    # if(GPIO)
