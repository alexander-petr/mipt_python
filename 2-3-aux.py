import RPi.GPIO  as f

leds = [ 2,3,4,17,27,22,18,9]
aux = [21,20,26,16,19,25,23,24]
f.setmode(f.BCM)

while True:
    for i in range  (8):
        f.setup(leds [i],f.OUT)
        f.setup (aux [i], f.IN)
        f.output (leds [i],f.input(aux [i]))
        
       
