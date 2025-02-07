## Team:
Belmondo Pietro  Bernardi Andrea  Gastaldi Andrea  Goletto Matteo  Fasulo Alice

## Idea del Nostro Progetto:
Il nostro progetto innovativo unisce tecnologia e riabilitazione per aiutare le persone affette da sclerosi multipla. L’idea alla base è semplice ma potente: trasformare i movimenti riabilitativi in un’attività interattiva e coinvolgente.
Abbiamo sviluppato un sistema in cui i pazienti, grazie a specifici movimenti, possono controllare un AlphaBot, un piccolo robot su due ruote. Il cuore del progetto è un joystick speciale, progettato e costruito interamente da noi, che utilizza un Micro:bit con accelerometro. Questo dispositivo rileva l’inclinazione del joystick e trasmette i dati a un secondo Micro:bit, collegato direttamente all’AlphaBot, permettendone il movimento. Inoltre all’interno del joystick abbiamo installato un motore che fa ruotare un disco in metallo, questa rotazione crea il principio di conservazione del moto angolare che suscita il force feedback, crea una piccola resistenza sul joystick che rende più difficile e realistico il movimento. In più abbiamo collegato una telecamera in streaming sull’Alphabot che grazie a un visore permette al paziente di vedere in tempo reale cosa vede l’Alphabot e quindi di conseguenza pilotarlo, anche da seduti o sdraiati.

## Realizzazione:
###  Come realizzare il Joystick : 
-Stampare con una stampante 3d 1 supporto che faccia da contenitore per il microbit,se ne trovano di diversi in rete. 
-Realizzare una base per appoggiare il  supporto del microbit in modo da collegare il microbit al tubo.
-Procurarsi un tubo cilindrico che faccia da impugnatura, l’impugnatura deve essere  cava all’interno.
-Collegare il motore al supporto delle 6 pile in modo da dare alimentazione, collegare insieme anche un potenziometro, in modo da poter controllare la potenza del motore.
-Inserire il tutto all’interno del tubo cavo e fissare il tutto con la colla a caldo.
-Chiudere il tubo con il supporto in legno che avrà fissato su di esso il supporto del microbit.
### MICROBIT
All’interno del nostro progetto abbiamo utilizzato due micro:bit. Sul primo abbiamo salvato il codice inviaMovimentiRegistrati.py, il cui scopo è rilevare i movimenti della persona e restituire in output una lettera che rappresenta il movimento rilevato:
"A" per avanti,
"I" per indietro,
"D" per destra,
"S" per sinistra,
"N" quando non si effettuano movimenti.
Questo micro:bit è stato posizionato sulla parte superiore di un joystick, da noi creato. In base al movimento del braccio, cambia l’output. La trasmissione dell’output avviene tramite onde radio, perciò è necessario importare nei codici dei due micro:bit la libreria radio, che consente la comunicazione tramite lo stesso canale. Tramite la funzione radio.send(), inviamo l’output al secondo micro:bit.Inoltre, quando viene rilevato il movimento "I" (indietro), il micro:bit emette dei suoni che simulano la retromarcia di un'auto. Per farlo, abbiamo importato la libreria music e utilizzato le sue funzioni per riprodurre il suono.
Il secondo micro:bit è collegato via USB all'AlphaBot, che lo alimenta e riceve in seriale i dati trasmessi dal micro:bit posizionato sul joystick. Su questo secondo micro:bit è salvato il codice riceveMovimentiRegistrati.py, il cui scopo è ricevere, tramite la funzione radio.receive(), il messaggio inviato dal primo micro:bit e trasmetterlo all'AlphaBot. 
È importante che entrambi i codici includano le librerie radio e microbit, e che i canali di trasmissione siano gli stessi, altrimenti i due dispositivi non potrebbero comunicare. Inoltre, entrambi i codici utilizzano la funzione sleep(), che stabilisce il tempo di trasmissione tra i due micro:bit. I valori impostati devono essere identici, altrimenti potrebbero verificarsi problemi di sincronizzazione.
## Obiettivo:
L’obiettivo è rendere la riabilitazione più motivante, trasformando quindi gli esercizi in un’esperienza più interattiva e stimolante. In questo modo, il paziente non solo svolge i movimenti terapeutici, ma riesce anche a svagarsi e divertirsi!

## Materiale utilizzato:
- 1 alphabot
- 2 microbit
- 1 raspberry pi camera v2 
- 2 supporti stampati con stampanti 3d
- 1 motore 
- 1 potenziometro da 1kΩ
- 1 supporto per 6 pile di tipo AA
- Jumper per collegamenti tra i componenti del controller
- 1 saldatrice a stagno
- Pistola per la colla a caldo 

## Librerie:
### Già installate (standard di Python):
- time
- io
- logging
- socket server
- http.server
- treading
- radio (per MicroBit)
- music (per MicroBit)
### Da installare (estrene): 
- RPi.GPIO (su Alphabot)
- picamera2 (su Alphabot)
- microbit
## Server:
Questo codice permette di trasmettere in diretta il video di una telecamera collegata a un Raspberry Pi, rendendolo visibile su un browser web. È pensato per collegare una telecamera a un robot (come l'Alphabot), ma può essere utilizzato con qualsiasi telecamera compatibile con Raspberry Pi.
Requisiti
Raspberry Pi con una telecamera compatibile (come la telecamera ufficiale di Raspberry Pi).
Python 3 installato sul Raspberry Pi.
Installazione ibreria Python:
picamera2: per accedere alla telecamera.
Come Funziona
Pagina Web di Streaming: Quando avvii il server, si apre una pagina web che mostra il video in diretta dalla telecamera. Il video è trasmesso come immagini JPEG (formato MJPEG) che il browser mostra in tempo reale.
Server Web: Il codice crea un server che ascolta sulla porta 8000 e rende disponibile il flusso video. Puoi accedere a questa pagina web dal browser di qualsiasi dispositivo sulla stessa rete del Raspberry Pi.
Esegui il file Python per avviare il server:
bash
Copia
python3 TestStreaming.py
Accedi al video: Una volta che il server è in esecuzione, apri un browser e vai all'indirizzo:
cpp
Copia
http://<indirizzo-ip-del-raspberry>:8000
Sostituisci <indirizzo-ip-del-raspberry> con l'indirizzo IP del Raspberry Pi.
Vedrai il flusso video in tempo reale dalla telecamera.
Nota
Assicurati che il Raspberry Pi e il dispositivo su cui visualizzi il video siano sulla stessa rete Wi-Fi.
La qualità del video dipende dalla tua connessione di rete.
Con queste informazioni, chiunque può facilmente configurare e utilizzare questo server per visualizzare il video dalla telecamera del Raspberry Pi su un browser web.


