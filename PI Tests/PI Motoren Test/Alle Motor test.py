# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep

M1in1 = 16
M1in2 = 18
M2in1 = 24
M2in2 = 29
M3in1 = 31
M3in2 = 33
M4in1 = 35
M4in2 = 37
M5in1 = 32
M5in2 = 36
M6in1 = 38
M6in2 = 40
M1en =  3 
M2en =  5 
M3en =  7 
M4en =  8 
M5en =  10 
M6en =  12

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(M1in1,GPIO.OUT)
GPIO.setup(M1in2,GPIO.OUT)
GPIO.output(M1in1,GPIO.LOW)
GPIO.output(M1in2,GPIO.LOW)

GPIO.setup(M2in1,GPIO.OUT)
GPIO.setup(M2in2,GPIO.OUT)
GPIO.output(M2in1,GPIO.LOW)
GPIO.output(M2in2,GPIO.LOW)

GPIO.setup(M3in1,GPIO.OUT)
GPIO.setup(M3in2,GPIO.OUT)
GPIO.output(M3in1,GPIO.LOW)
GPIO.output(M3in2,GPIO.LOW)

GPIO.setup(M4in1,GPIO.OUT)
GPIO.setup(M4in2,GPIO.OUT)
GPIO.output(M4in1,GPIO.LOW)
GPIO.output(M4in2,GPIO.LOW)

GPIO.setup(M5in1,GPIO.OUT)
GPIO.setup(M5in2,GPIO.OUT)
GPIO.output(M5in1,GPIO.LOW)
GPIO.output(M5in2,GPIO.LOW)

GPIO.setup(M6in1,GPIO.OUT)
GPIO.setup(M6in2,GPIO.OUT)
GPIO.output(M6in1,GPIO.LOW)
GPIO.output(M6in2,GPIO.LOW)


p1=GPIO.PWM(M1en,1000)
p2=GPIO.PWM(M2en,1000)
p3=GPIO.PWM(M3en,1000)
p4=GPIO.PWM(M4en,1000)
p5=GPIO.PWM(M5en,1000)
p6=GPIO.PWM(M6en,1000)


p1.start(3)
p2.start(5)
p3.start(7)
p4.start(8)
p5.start(10)
p6.start(12)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(M1in1,GPIO.HIGH)
         GPIO.output(M1in2,GPIO.LOW)
         GPIO.output(M2in1,GPIO.HIGH)
         GPIO.output(M2in2,GPIO.LOW)
         GPIO.output(M3in1,GPIO.HIGH)
         GPIO.output(M3in2,GPIO.LOW)
         GPIO.output(M4in1,GPIO.HIGH)
         GPIO.output(M4in2,GPIO.LOW)
         GPIO.output(M5in1,GPIO.HIGH)
         GPIO.output(M5in2,GPIO.LOW)
         GPIO.output(M6in1,GPIO.HIGH)
         GPIO.output(M6in2,GPIO.LOW)
         
         print("forward")
         x='z'
        else:
         GPIO.output(M1in1,GPIO.LOW)
         GPIO.output(M1in2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(M1in1,GPIO.LOW)
        GPIO.output(M1in2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(M1in1,GPIO.HIGH)
        GPIO.output(M1in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(M1in1,GPIO.LOW)
        GPIO.output(M1in2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")