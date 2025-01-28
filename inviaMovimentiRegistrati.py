from microbit import *
import radio


radio.on()
radio.config(group=23)


uart.init(baudrate=9600, tx=pin0, rx=pin1)


# Funzione per controllare inclinazione sull'asse Y (Avanti/Indietro)
def controllo_avanti_indietro():
    y = accelerometer.get_y()
    if y > 400:
        return "I"  # avanti
    elif y < -400:
        return "A"  # indietro
    else:
        return "N"  # neutrale

# Funzione per controllare inclinazione sull'asse X (Sinistra/Destra)
def controllo_sinistra_destra():
    x = accelerometer.get_x()
    if x > 400:
        return "D"  # destra
    elif x < -400:
        return "S"  # sinistra
    else:
        return "N"  # neutrale

while True:
    # Controlla le inclinazioni
    movimento_y = controllo_avanti_indietro()
    movimento_x = controllo_sinistra_destra()

    # Invia i comandi rilevati via radio
    if movimento_y != "N":
        display.show(movimento_y)  # Mostra il comando sul display
        uart.write(movimento_y)
        #radio.send(movimento_y)

    elif movimento_x != "N":
        display.show(movimento_x)  # Mostra il comando sul display
        uart.write(movimento_x)
        #radio.send(movimento_x)
    
    else:
        display.show("N")  # Stato neutrale
        uart.write("N")
        #radio.send("N")
    
    sleep(1000)