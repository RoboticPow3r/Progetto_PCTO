from microbit import *
import radio
radio.on()
radio.config(group=23)


while True:
    message = radio.receive()
    if message:
        display.show(message)
        print(message) #manda messaggio sulla seriale
    sleep(100)