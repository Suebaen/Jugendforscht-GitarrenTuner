import RPI.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en1= 25
temp1 = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p = GPIO.PWM(en1,1000)



p.start(25)


while (1):
    x=raw_input()
    

    if( x== 'r'):
        print("run")
        if (temp1==1):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            print("Es dreht sich")
            sleep(5)
            x = 'z'
    if (x=='z'):
         print("STOP")
        if (temp1==1):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            print("Der Motor sollte jetzt stehen")
            sleep(5)
