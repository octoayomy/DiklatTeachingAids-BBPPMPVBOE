from machine import ADC, Pin
import time
adc = machine.ADC(4)
led = Pin("LED", Pin.OUT)
led.low()

while True:
    ADC_voltage = adc.read_u16() * (3.3 / (65536))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    temp_fahrenheit=32+(1.8*temperature_celcius)
    
    if temperature_celcius >36:
        print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit))
        led.value (1)
        time.sleep_ms(1000)
    
    elif temperature_celcius <35:
        print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit))
        led.value (0)
        time.sleep_ms(1000)