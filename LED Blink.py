from machine import Pin
import utime

led = Pin(LED, Pin.OUT)
led.low()

while True:
    led.value(1)
    utime.sleep(1)
    
    led.value(0)
    utime.sleep(1)