import time
import _thread
import machine
import utime




# main program
_thread.start_new_thread(led_task, (10, 0.5))
sensor_task(10, 0.5)
