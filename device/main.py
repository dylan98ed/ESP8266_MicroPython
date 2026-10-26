
from machine import Pin
from time import sleep_ms

# LED integrado en NodeMCU ESP8266
# GPIO2 corresponde a D4
led = Pin(2, Pin.OUT, value=1)

while True:
    led.value(0)  # Encender LED
    sleep_ms(1000)

    led.value(1)  # Apagar LED
    sleep_ms(1000)
