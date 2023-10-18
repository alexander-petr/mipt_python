import RPi.GPIO  as GPIO


GPIO.setmode (GPIO.BCM)
GPIO.setup (11,GPIO.OUT)
GPIO.setup (24,GPIO.OUT)
try:
    pers = int (input ('input %'))
    p = GPIO.PWM (11,1000)
    p.start (pers)
    q = GPIO.PWM (24,1000)
    q.start (pers)
    input ('stop: ')
    p.stop()
    q.stop()
finally:
     GPIO.output (24,0)
     GPIO.cleanup()