import RPi.GPIO  as f
import time as t
leds = [ 2,3,4,17,27,22,18,9]
f.setmode(f.BCM)
f.setup(leds,f.OUT)
f.output (leds,1)
f.output (leds,0)
for j in range (3):
    for i in range (8):
        f.output (leds[i],1)
        t.sleep (0.2)
        f.output (leds[i],0)
f.output(leds,0)
f.cleanup()        