from machine import Pin
# Define the inputs and outputs and assign them to software objects
# First argument is a GPIO pin number, rather than a physical pin number
led1 = Pin(16, Pin.OUT)
sw5 = Pin(13, Pin.IN, Pin.PULL_UP)
while True:
# Control the LED output values, based on the received button input
    if sw5.value() == 1:
        led1.on()
        print(sw5.value())
    else:
        led1.off()
        print(sw5.value())