## Team:
Belmondo Pietro  Bernardi Andrea  Gastaldi Andrea  Goletto Matteo  Fasulo Alice

## Idea del Nostro Progetto:
Il nostro progetto innovativo unisce tecnologia e riabilitazione per aiutare le persone affette da sclerosi multipla. L’idea alla base è semplice ma potente: trasformare i movimenti riabilitativi in un’attività interattiva e coinvolgente.
Abbiamo sviluppato un sistema in cui i pazienti, grazie a specifici movimenti, possono controllare un AlphaBot, un piccolo robot su due ruote. Il cuore del progetto è un joystick speciale, progettato e costruito interamente da noi, che utilizza un Micro:bit con accelerometro. Questo dispositivo rileva l’inclinazione del joystick e trasmette i dati a un secondo Micro:bit, collegato direttamente all’AlphaBot, permettendone il movimento. Inoltre all’interno del joystick abbiamo installato un motore che fa ruotare un disco in metallo, questa rotazione crea il principio di conservazione del moto angolare che suscita il force feedback, crea una piccola resistenza sul joystick che rende più difficile e realistico il movimento. In più abbiamo collegato una telecamera in streaming sull’Alphabot che grazie a un visore permette al paziente di vedere in tempo reale cosa vede l’Alphabot e quindi di conseguenza pilotarlo, anche da seduti o sdraiati.

## Realizzazione:
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


