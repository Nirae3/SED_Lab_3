from machine import ADC
from machine import Pin
from time import sleep

# Set up ADC for pin GP26 (physical pin 31)
# Note: You could also use GP27 (ADC1) or GP28 (ADC2)
led1 = Pin(16, Pin.OUT)
adc_pin = ADC(26)
asdfasdfaf

while True:
    # Read the analog value (0-65535)
    raw_value = adc_pin.read_u16()
    print(f"Analog Value: {raw_value}")

    # Convert to a voltage (optional)
    voltage = raw_value * (3.3 / 65535)
    print(f"Voltage: {voltage:.2f}V")
    if raw_value>20000:
        led1.on()
    else:
        led1.off()

    sleep(1)
