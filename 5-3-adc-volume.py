import RPi.GPIO as GPIO
import time
def binary(n):
    return[int(i) for i in bin(n)[2:].zfill(8)]
def adc(troyka):
    value = 0
    for i in range (7, -1, -1):
        value += 2**i
        GPIO.output(dac, binary(value))
        time.sleep (0.05)
        if GPIO.input(comp) == 1:
            value -= 2**i
    return value
def g(value):
    for i in range(8,0,-1):
        if i*32 - 1 <=value:
            return binary(2**i - 1)
dac = (8, 11, 7, 1, 0, 5, 12, 6)
leds = (2, 3, 4, 17, 27, 22, 10, 9)
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
for i in range (8):
        GPIO.setup(leds[i], 0)
while True:
    GPIO.output(leds, g(adc(troyka)))