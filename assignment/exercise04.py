"""
Use analog input with photocell
"""

import time
import machine

led = machine.Pin("LED", machine.Pin.OUT)
adc = machine.ADC(28)

blink_period = 0.1

max_bright = 45195
min_bright = 256

while True:
    value = adc.read_u16()
    print(value)
    duty_cycle = (value - min_bright) / (max_bright - min_bright)
    led.high()
    time.sleep(blink_period * duty_cycle)
    led.low()
    time.sleep(blink_period * (1 - duty_cycle))
