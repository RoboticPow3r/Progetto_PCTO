import io  # Modulo per gestire operazioni di input/output in memoria
import logging  # Modulo per la gestione dei log
import socketserver  # Modulo per creare server socket basati su TCP/IP
from http import server  # Modulo per creare un server HTTP
from threading import Condition  # Modulo per la gestione della sincronizzazione tra thread

# Importazioni specifiche per la gestione della fotocamera Raspberry Pi
from picamera2 import Picamera2  # Classe per gestire la fotocamera
from picamera2.encoders import JpegEncoder  # Codificatore per il formato JPEG
from picamera2.outputs import FileOutput  # Classe per gestire l'output del video

# Definizione della pagina HTML che verrà servita ai client
PAGE = """
<html>
<head>
<title>Telecamera RoboticPow3r!!!</title>
  <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
            background-color: #000;
        }
        .contenitore {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            height: 100%;
            width: 100%;
        }
        img {
            width: 49%;
            height: 100%;
            object-fit: cover;
        }

        @media (max-width: 768px) {
            .video-container {
                flex-direction: column;
            }
            video {
                width: 100%;
                height: 50%;
            }
        }
    </style>
</head>
<body>
<div id="contenitore"> 
     <img src="stream.mjpg" / >
     <img src="stream.mjpg" / >
</div>
</body>
</html>
"""

# Classe per gestire lo streaming video
class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None  # Memorizza il frame più recente
        self.condition = Condition()  # Variabile di condizione per la sincronizzazione

    def write(self, buf):
        with self.condition:
            self.frame = buf  # Aggiorna il frame corrente
            self.condition.notify_all()  # Notifica ai client che un nuovo frame è disponibile

# Gestore delle richieste HTTP
class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)  # Reindirizzamento alla pagina principale
            self.send_header('Location', '/index.html')  # Indirizza verso index.html
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')  # Codifica la pagina HTML in bytes
            self.send_response(200)  # Risponde con codice 200 OK
            self.send_header('Content-Type', 'text/html')  # Imposta il tipo di contenuto
            self.send_header('Content-Length', len(content))  # Imposta la lunghezza del contenuto
            self.end_headers()
            self.wfile.write(content)  # Invia la pagina HTML al client
        elif self.path == '/stream.mjpg':
            self.send_response(200)  # Risponde con codice 200 OK
            self.send_header('Age', 0)  # Evita caching del flusso video
            self.send_header('Cache-Control', 'no-cache, private')  # Impedisce caching da parte del browser
            self.send_header('Pragma', 'no-cache')  # Imposta un'intestazione aggiuntiva per evitare cache
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')  # Imposta il formato per lo streaming MJPEG
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()  # Attende un nuovo frame
                        frame = output.frame  # Recupera il frame attuale
                    self.wfile.write(b'--FRAME\r\n')  # Inizia un nuovo frame
                    self.send_header('Content-Type', 'image/jpeg')  # Imposta il tipo di contenuto
                    self.send_header('Content-Length', len(frame))  # Imposta la lunghezza dell'immagine
                    self.end_headers()
                    self.wfile.write(frame)  # Invia il frame al client
                    self.wfile.write(b'\r\n')  # Aggiunge una nuova riga
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))  # Logga eventuali errori
        else:
            self.send_error(404)  # Risponde con errore 404 se la risorsa non è trovata
            self.end_headers()

# Server HTTP multithread per gestire più connessioni contemporaneamente
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True  # Permette di riutilizzare l'indirizzo IP senza attese
    daemon_threads = True  # Usa thread daemon per la gestione delle richieste

# Configurazione e avvio della fotocamera
picam2 = Picamera2()  # Istanza della fotocamera
picam2.configure(picam2.create_video_configuration(main={"size": (1280, 720)}))  # Configura la risoluzione video
picam2.set_controls({"ScalerCrop": (0, 0, 3280, 2464)})  # Massimizza il campo visivo
output = StreamingOutput()  # Crea un'istanza dell'output per lo streaming
picam2.start_recording(JpegEncoder(), FileOutput(output))  # Avvia lo streaming della videocamera

# Avvio del server HTTP
try:
    address = ('0.0.0.0', 8000)  # Ascolta su tutte le interfacce di rete alla porta 8000
    server = StreamingServer(address, StreamingHandler)  # Crea il server con l'handler definito
    server.serve_forever()  # Mantiene il server in esecuzione
finally:
    picam2.stop_recording()  # Ferma la registrazione quando il server viene chiuso