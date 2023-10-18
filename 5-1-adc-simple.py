import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12 ,6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return[int(value) for value in bin(value)[2:].zfill(8)]

def adc():
    for i in range (256):
        signal = decimal2binary(i)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        compvalue = GPIO.input(comp)
        if compvalue == 1:
            print (i, (i/256) * 3.3, "V")
            break

try:
    for j in range (100):
        adc()

finally:
    GPIO.output(dac,0)
    GPIO.cleanup