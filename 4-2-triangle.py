import RPi.GPIO  as GPIO
from time import sleep

GPIO.setmode (GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)

def decimal2binary(value):
    return [int (value) for value in bin(value)[2:]. zfill(8)]

try:
    while (True):
        period = input ('Введите число от 0 до 255:')
        if not period.isdigit():
            print("this is not natural number")
        d = int(period) / 512
        for i in range (256):
             GPIO.output (dac, decimal2binary(i))
             sleep(d)
        for i in range (255, -1, -1):
            GPIO.output (dac, decimal2binary(i))
            sleep(d)


finally:
    GPIO.output (dac,1)
    GPIO.cleanup()