from machine import Pin
import time

sw5 = Pin(13, Pin.IN, Pin.PULL_UP)

sw5.off()
print(sw5.value())

while True:
    print(sw5.value())
    time.sleep(0.5)
