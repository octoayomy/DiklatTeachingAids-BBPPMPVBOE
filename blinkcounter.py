from machine import Pin
#import utime
import time

led = Pin("LED", Pin.OUT)
led.low()
total_seconds = 10

while total_seconds > 0:
    minutes, seconds = divmod(total_seconds,60)
    print ("Hitung Mundur:{:02d}:{:02d}".format(minutes, seconds))
    time.sleep(1)
    #led.value(0)
    total_seconds -=1
if True:
    led.value(1)
    print ("Lampu ON")
    time.sleep (10)
    led.value(0)
    print ("Lampu OFF")
    
   