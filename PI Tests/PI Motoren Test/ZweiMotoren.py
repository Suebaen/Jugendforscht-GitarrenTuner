import RPi.GPIO as GPIO
from time import sleep
def test():
    GPIO.setmode(GPIO.BOARD)

    m1 = 7
    m2 = 5
    m3 = 3


    m1a = 23
    m2a = 21
    m3a = 19

    m1b = 33
    m2b = 31
    m3b = 29

    m1c = 40
    m2c = 37
    m3c = 35


    m1d = 38
    m2d = 36
    m3d = 32

    m1e = 26
    m2e = 24
    m3e = 22

    GPIO.setup(m1,GPIO.OUT)
    GPIO.setup(m2,GPIO.OUT)
    GPIO.setup(m3,GPIO.OUT)

    GPIO.setup(m1a,GPIO.OUT)
    GPIO.setup(m2a,GPIO.OUT)
    GPIO.setup(m3a,GPIO.OUT)

    GPIO.setup(m1b,GPIO.OUT)
    GPIO.setup(m2b,GPIO.OUT)
    GPIO.setup(m3b,GPIO.OUT)

    GPIO.setup(m1c,GPIO.OUT)
    GPIO.setup(m2c,GPIO.OUT)
    GPIO.setup(m3c,GPIO.OUT)

    GPIO.setup(m1d,GPIO.OUT)
    GPIO.setup(m2d,GPIO.OUT)
    GPIO.setup(m3d,GPIO.OUT)

    GPIO.setup(m1e,GPIO.OUT)
    GPIO.setup(m2e,GPIO.OUT)
    GPIO.setup(m3e,GPIO.OUT)

    print("Forward")
    GPIO.output(m1,GPIO.HIGH)
    GPIO.output(m2,GPIO.LOW)
    GPIO.output(m3,GPIO.HIGH)
    sleep(1)
    GPIO.output(m1a,GPIO.HIGH)
    GPIO.output(m2a,GPIO.LOW)
    GPIO.output(m3a,GPIO.HIGH)
    sleep(1)
    GPIO.output(m1b,GPIO.HIGH)
    GPIO.output(m2b,GPIO.LOW)
    GPIO.output(m3b,GPIO.HIGH)
    sleep(1)
    GPIO.output(m1c,GPIO.HIGH)
    GPIO.output(m2c,GPIO.LOW)
    GPIO.output(m3c,GPIO.HIGH)
    sleep(1)
    GPIO.output(m1d,GPIO.HIGH)
    GPIO.output(m2d,GPIO.LOW)
    GPIO.output(m3d,GPIO.HIGH)
    sleep(1)
    GPIO.output(m1e,GPIO.HIGH)
    GPIO.output(m2e,GPIO.LOW)
    GPIO.output(m3e,GPIO.HIGH)

    sleep(4)

    print("BAckward")
    GPIO.output(m2,GPIO.HIGH)
    GPIO.output(m3,GPIO.LOW)
    sleep(1)
    GPIO.output(m2a,GPIO.HIGH)
    GPIO.output(m3a,GPIO.LOW)
    sleep(1)
    GPIO.output(m2b,GPIO.HIGH)
    GPIO.output(m3b,GPIO.LOW)
    sleep(1)
    GPIO.output(m2c,GPIO.HIGH)
    GPIO.output(m3c,GPIO.LOW)
    sleep(1)
    GPIO.output(m2d,GPIO.HIGH)
    GPIO.output(m3d,GPIO.LOW)
    sleep(1)
    GPIO.output(m2e,GPIO.HIGH)
    GPIO.output(m3e,GPIO.LOW)


    sleep(4)

    print ("STOP")
    GPIO.output(m3,GPIO.LOW)
    GPIO.output(m3a,GPIO.LOW)
    GPIO.output(m3b,GPIO.LOW)
    GPIO.output(m3c,GPIO.LOW)
    GPIO.output(m3d,GPIO.LOW)
    GPIO.output(m3e,GPIO.LOW)
    GPIO.cleanup()