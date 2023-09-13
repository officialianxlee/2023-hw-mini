"""
Response time and Light intensity - double-threaded
"""

import machine
import time
import random
import json
import sys 
import os
import _thread
import utime

led = machine.Pin("LED", machine.Pin.OUT)
button1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
adc = machine.ADC(28)

N: int = 5
sample_ms = 10.0
on_ms = 500

is_micropython = sys.implementation.name == "micropython"

if not is_micropython:
    import os.path

def get_params(param_file: str) -> dict:
    """Reads parameters from a JSON file."""
    
    if not is_regular_file(param_file):
        raise OSError(f"File {param_file} not found")

    with open(param_file) as f:
        params = json.load(f)

    return params

def is_regular_file(path: str) -> bool:
    """Checks if a regular file exists."""
    
    if not is_micropython:
        return os.path.isfile(path)

    S_IFREG = 0x8000

    try:
        return os.stat(path)[0] & S_IFREG != 0
    except OSError:
        return False

# Load parameters from JSON file
params = get_params('project02.json')
N = params.get("N", 10)
sample_ms = params.get("sample_ms", 10.0)
on_ms = params.get("on_ms", 500)

blink_period = 0.1
max_bright = 20000
min_bright = 10000

game_over = False

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)

def blinker(N: int) -> None:
    """let user know game started / is over"""
    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)

def led_task(N, sleep_time):
    global game_over
    t1 = [None] * N
    t2 = [None] * N

    blinker(3)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))
        led.high()
        tic = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), tic) < on_ms:
            if button1.value() == 0:
                t1[i] = utime.ticks_diff(utime.ticks_ms(), tic)
                led.low()
            if button2.value() == 0:
                t2[i] = utime.ticks_diff(utime.ticks_ms(), tic)
                led.low()
        led.low()

    blinker(5)

    # Collate results and write to JSON file
    results = []

    for i, t in enumerate([t1, t2]):
        player_num = i + 1
        misses = t.count(None)
        print(f"Player {player_num} missed the light {misses} / {N} times")

        t_good = [x for x in t if x is not None]

        if t_good:
            avg_response_time = sum(t_good) / len(t_good)
            min_response_time = min(t_good)
            max_response_time = max(t_good)
        else:
            avg_response_time = min_response_time = max_response_time = None

        print(f"Player {player_num} Average response time: {avg_response_time} ms")
        print(f"Player {player_num} Minimum response time: {min_response_time} ms")
        print(f"Player {player_num} Maximum response time: {max_response_time} ms")

        results.append({
            f"Player {player_num} response_times": t,
            f"Player {player_num} score": f"{N - misses}/{N} flashes",
            f"Player {player_num} average_response_time": avg_response_time,
            f"Player {player_num} min_response_time": min_response_time,
            f"Player {player_num} max_response_time": max_response_time,
        })

    with open('project02results.json', 'w') as file:
        json.dump(results, file)

    print("Results saved to project02results.json")

    # Set game_over to True at the end of the main function to signal the end of the game
    game_over = True


def sensor_task(N, sleep_time):
    values = []
    while not game_over:
        value = adc.read_u16()
        values.append(value)
        time.sleep(blink_period)

    # Save data at the end of the game
    max_value = max(values)
    min_value = min(values)
    
    data = {
        "values": values,
        "max_value": max_value,
        "min_value": min_value
    }
    
    with open('light_intensity.json', 'w') as json_file:
        json.dump(data, json_file)
    
    print(f"Light intensity data written to JSON file with max value: {max_value} and min value: {min_value}")

# main program
_thread.start_new_thread(led_task, (10, 0.5))
sensor_task(10, 0.5)

