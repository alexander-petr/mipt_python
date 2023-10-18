import RPi.GPIO  as GPIO
import sys

GPIO.setmode (GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)
def decimal2binary(value):
    return [int (value) for value in bin(value)[2:]. zfill(8)]

try:
    while (True):
        x=input ('Введите число от 0 до 255:')
        if x== 'q':
            break
        elif not x.isdigit():
            print ("This is not natural numbers in the interval [0;255]")
        elif  not 0<=int (x) <=255 :
            print ("This is not natural numbers in the interval [0;255]")
        elif x.count('.')!=0:
            print ("This is not natural numbers in the interval [0;255]")    
        elif 0<=int (x) <=255 and x.isdigit():
            GPIO.output (dac, decimal2binary(int(x)))
            print ("{:.4f}". format(int(x) * 3.3 / 256))
            continue
        else:
            print ("Number outside the interval of natural numbers [0;255]")
            continue
finally:
     GPIO.output (dac,0)
     GPIO.cleanup()