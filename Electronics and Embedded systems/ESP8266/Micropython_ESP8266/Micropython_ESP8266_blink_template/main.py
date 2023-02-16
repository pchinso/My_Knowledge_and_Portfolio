from machine import Pin
import time

led = Pin(16, Pin.OUT)

while True:
    led.on()
    time.sleep(2.5)
    led.off()
    time.sleep(2.5)