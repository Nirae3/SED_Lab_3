from machine import Pin, ADC  # Import Pin and ADC modules
import time  # Import time module for delays

led1 = Pin(18, Pin.OUT)
pot = ADC(26)    

while True:
    value = pot.read_u16() #  Read the potentiometer value (range: 0 to 65535)
    delay = 0.05 + (value / 65535) * 1.0  # convert the value to a delay time between 0.05 and 1.05 seconds
    led1.toggle() # toggle the led
    time.sleep(delay) # wait for calculated delated time