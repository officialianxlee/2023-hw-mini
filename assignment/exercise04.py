import time
import machine
import json

led = machine.Pin("LED", machine.Pin.OUT)
adc = machine.ADC(28)

blink_period = 0.1

max_bright = 20000
min_bright = 10000

values = []

try:
    while True:
        value = adc.read_u16()
        values.append(value)
        
        duty_cycle = (value - min_bright) / (max_bright - min_bright)
        led.high()
        time.sleep(blink_period * duty_cycle)
        led.low()
        time.sleep(blink_period * (1 - duty_cycle))
except KeyboardInterrupt:
    # When the loop is interrupted, find max and min values and write to JSON
    max_value = max(values)
    min_value = min(values)
    
    data = {
        "values": values,
        "max_value": max_value,
        "min_value": min_value
    }
    
    with open('exercise04.json', 'w') as json_file:
        json.dump(data, json_file)
    
    print(f"Data written to JSON file with max value: {max_value} and min value: {min_value}")
