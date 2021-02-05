# import numpy as np
import RPi.GPIO as GPIO
from subprocess import call

print("Pleas press one of the buttons")
A=input("Schreib ein A: \n")
C=input("Schreib ein C: \n")
D=input("Schreib ein D: \n")
F=input("Schreib ein F: \n")
G=input("Schreib ein G: \n")

print (A)
print (C)
print (D)
print (F)
print (G)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.OUT)

class CallPy(object):
    
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasA.py'):
        self.path =path
    
    def  call_python_file(self):
        call(["Python3", "{}".format(self.path)])
class CallPy2(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasC.py'):
        self.path =path
    
    def  call_python_file2(self):
        call(["Python3", "{}".format(self.path)])
class CallPy3(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasD.py'):
        self.path =path
    
    def  call_python_file3(self):
        call(["Python3", "{}".format(self.path)])
class CallPy4(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasE.py'):
        self.path =path
    
    def  call_python_file4(self):
        call(["Python3", "{}".format(self.path)])

class CallPy5(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasF.py'):
        self.path =path
    
    def  call_python_file5(self):
        call(["Python3", "{}".format(self.path)])

class CallPy6(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasG.py'):
        self.path =path
    
    def  call_python_file6(self):
        call(["Python3", "{}".format(self.path)])

while (True):


    if (A == 'A'):
        c= CallPy()
        c.call_python_file()

    if(C == 'C'):
        c= CallPy2()
        c.call_python_file2()

    if(D == 'D'):        
        c= CallPy3()
        c.call_python_file3()

    if(E == 'E'):
        c= CallPy4()
        c.call_python_file4()

    if(F == 'F'):
        c= CallPy5()
        c.call_python_file5()

    if(G == 'G'):
        c= CallPy6()
        c.call_python_file6()

    if(GPIO.input(11)== True):
        GPIO.output(13, True)
        sleep (0.1)
        print("Hello")
    else:
        GPIO.output (13,False)
        GPIO.cleanup