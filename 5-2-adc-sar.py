import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12 ,6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

s = (1, 1, 1, 1, 1, 1, 1, 1)

def adc():
    c = 0
    for i in range (7, -1, -1):
        signal = decimal2binary(c)
        GPIO.output(dac, signal)
        c+= 2 ** i
        time.sleep(0.001)
        compvalue = GPIO.input(comp)
        if compvalue == 1:
            c -= 2** i
        print ((c/256)* 3.3, "V")
            

try:
    for j in range (100):
        adc()

finally:
    GPIO.output(dac,0)
    GPIO.cleanup