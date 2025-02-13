from microbit import *
import radio
import music

radio.on()
radio.config(group=23)

# Funzione per controllare inclinazione sull'asse Y (Avanti/Indietro)
def controllo_avanti_indietro():
    y = accelerometer.get_y()
    if y > 600:
        music.set_tempo(bpm=150)
        music.play(music.BA_DING)
        music.set_tempo(bpm=150)
        return "I"  # avanti
    elif y < -600:
        return "A"  # indietro
    else:
        return "N"  # neutrale

# Funzione per controllare inclinazione sull'asse X (Sinistra/Destra)
def controllo_sinistra_destra():
    x = accelerometer.get_x()
    if x > 600:
        return "D"  # destra
    elif x < -600:
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
        radio.send(movimento_y)

    elif movimento_x != "N":
        display.show(movimento_x)  # Mostra il comando sul display
        radio.send(movimento_x)
    
    else:
        display.show("N")  # Stato neutrale
        radio.send("N")
    
    sleep(100)
