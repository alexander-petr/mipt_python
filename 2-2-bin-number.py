import RPi.GPIO  as f
import time as t
dac= 8,11,7,1,0,5,12,6
number=0,0,0,0,0,0,1,0
f.setmode(f.BCM)
f.setup(dac,f.OUT)
for i in range (8):
    f.output(dac[i],number[i])
t.sleep(15)
f.setup(dac,0)
f.cleanup()