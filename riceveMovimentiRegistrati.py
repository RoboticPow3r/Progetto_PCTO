# Imports go at the top
from microbit import *
import radio
radio.on()
radio.config(group=23)


while True:
    message = radio.receive()
    if message:
        display.show(message)

    sleep(200)