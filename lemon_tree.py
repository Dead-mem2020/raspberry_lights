import machine
import time 

Pin1 = machine.Pin(0, machine.Pin.OUT)
Pin2 = machine.Pin(1, machine.Pin.OUT)

while True:
    Pin1.value(1)
    Pin2.value(0)
    time.sleep(0.1)
    Pin1.value(0)
    Pin2.value(1)
    time.sleep(0.1)