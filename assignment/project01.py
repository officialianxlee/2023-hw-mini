"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import sys 
import os


led = Pin("LED", Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_UP)

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
params = get_params('project01.json')
N = params.get("N", 10)
sample_ms = params.get("sample_ms", 10.0)
on_ms = params.get("on_ms", 500)



def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


t: list[float | None] = []

blinker(3)

for i in range(N):
    time.sleep(random_time_interval(0.5, 5.0))

    led.high()

    tic = time.ticks_ms()
    t0 = None
    while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
        if button.value() == 0:
            t0 = time.ticks_diff(time.ticks_ms(), tic)
            led.low()
            break
    t.append(t0)

    led.low()

blinker(5)

# %% collate results
misses = t.count(None)
print(f"You missed the light {misses} / {N} times")

t_good = [x for x in t if x is not None]

# Calculate and print the average, min, max response time
if t_good:
    avg_response_time = sum(t_good) / len(t_good)
    min_response_time = min(t_good)
    max_response_time = max(t_good)
else:
    avg_response_time = min_response_time = max_response_time = None

print(f"Average response time: {avg_response_time} ms")
print(f"Minimum response time: {min_response_time} ms")
print(f"Maximum response time: {max_response_time} ms")

# Write results to JSON file
results = {
    "response_times": t,
    "score": str(misses)+ "/" +str(N) + " flashes",
    "average_response_time": avg_response_time,
    "min_response_time": min_response_time,
    "max_response_time": max_response_time,
}

with open('project01results.json', 'w') as file:
    json.dump(results, file)

print(t_good)
