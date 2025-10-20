from machine import Pin
import time

led = Pin(16, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

led_state = False  # LED off at start
previous_state = 0

while True:
    current_state = sw5.value()
    if current_state == 1 and previous_state == 0:  # button pressed
        time.sleep(0.5)  # delay by 5 ms
        if sw5.value() == 1: # if button still pressed
            led_state = not led_state  # toggle/change the state
            led.value(led_state) # update the value of led to the led state
    previous_state = current_state # for iteration, store the value in the previous state