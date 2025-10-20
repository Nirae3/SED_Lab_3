
"""
2. Make the potentiometer control the blinking interval of the LED in the first code example.
3. Use PWM to make a "breathing" LED, i.e. the LED should gradually fade in and out, in terms of
its brightness, periodically, as if it was breathing.
"""

from machine import Pin, PWM
import time

led1 = PWM(Pin(18))
led1.freq(1000)

while True:
    # Fade in
    for duty in range(0, 65536, 500):
        led1.duty_u16(duty)
        time.sleep(0.01)

    # Fade out
    for duty in range(65535, -1, -500):
        led1.duty_u16(duty)
        time.sleep(0.01)