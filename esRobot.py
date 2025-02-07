import RPi.GPIO as GPIO  # Importa la libreria per controllare i GPIO della Raspberry Pi
import time  # Importa la libreria per gestire i ritardi temporali
import threading, queue  # Importa le librerie per la gestione dei thread e delle code
import serial  # Importa la libreria per la comunicazione seriale

q = queue.Queue()  # Crea una coda per la comunicazione tra thread

class AlphaBot(object):
    def __init__(self, in1=12, in2=13, ena=6, in3=20, in4=21, enb=26):
        self.IN1 = in1  # Pin per il controllo del motore destro
        self.IN2 = in2  # Pin per il controllo del motore destro
        self.IN3 = in3  # Pin per il controllo del motore sinistro
        self.IN4 = in4  # Pin per il controllo del motore sinistro
        self.ENA = ena  # Pin per il controllo della velocità del motore destro
        self.ENB = enb  # Pin per il controllo della velocità del motore sinistro

        GPIO.setmode(GPIO.BCM)  # Imposta la numerazione dei pin su schema BCM
        GPIO.setwarnings(False)  # Disabilita gli avvisi sui pin già usati
        
        # Configura i pin come output
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        
        # Imposta PWM per il controllo della velocità dei motori
        self.PWMA = GPIO.PWM(self.ENA, 500)  # Frequenza PWM di 500 Hz
        self.PWMB = GPIO.PWM(self.ENB, 500)
        self.PWMA.start(50)  # Avvia il PWM con duty cycle al 50%
        self.PWMB.start(50)

    def forward(self):  # Movimento in avanti
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

    def stop(self):  # Ferma i motori
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def backward(self):  # Movimento all'indietro
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

    def left(self):  # Rotazione a sinistra
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

    def right(self):  # Rotazione a destra
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def setPWMA(self, value):  # Modifica la velocità del motore destro
        self.PWMA.ChangeDutyCycle(value)

    def setPWMB(self, value):  # Modifica la velocità del motore sinistro
        self.PWMB.ChangeDutyCycle(value)    
    
    def setMotor(self, left, right):  # Controllo personalizzato dei motori
        if (right >= 0) and (right <= 100):
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
            self.PWMA.ChangeDutyCycle(right)
        elif (right < 0) and (right >= -100):
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
            self.PWMA.ChangeDutyCycle(-right)
        if (left >= 0) and (left <= 100):
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
            self.PWMB.ChangeDutyCycle(left)
        elif (left < 0) and (left >= -100):
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.HIGH)
            self.PWMB.ChangeDutyCycle(-left)

class Read_Microbit(threading.Thread):  # Classe per leggere dati dalla porta seriale
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
    
    def terminate(self):  # Ferma il thread
        self._running = False
        
    def run(self):  # Funzione principale del thread
        port = "/dev/ttyACM0"  # Porta seriale della micro:bit
        s = serial.Serial(port)  # Inizializza la connessione seriale
        s.baudrate = 115200  # Imposta la velocità di trasmissione dati
        while True:
            data = s.readline().decode()[:-1]  # Legge e decodifica il messaggio ricevuto
            q.put(data)  # Inserisce il messaggio nella coda
            time.sleep(0.1)  # Ritardo per evitare sovraccarico
            
def main():
    robot = AlphaBot()  # Crea un'istanza del robot
    rm = Read_Microbit()  # Crea un'istanza del thread per leggere dalla micro:bit
    rm.start()  # Avvia il thread
    while True:        
        message = q.get()  # Legge un messaggio dalla coda
        q.task_done()  # Segnala che il messaggio è stato elaborato
        print("Arrivato")
        message = str(message)[:-1]  # Converte il messaggio in stringa
        print(message)
    
        if message == "A":  # Se il messaggio ricevuto è "A", il robot avanza
            robot.forward()
        elif message == "I":  # Se il messaggio ricevuto è "I", il robot indietreggia
            robot.backward()
        elif message == "S":  # Se il messaggio ricevuto è "S", il robot gira a sinistra
            robot.left()
        elif message == "D":  # Se il messaggio ricevuto è "D", il robot gira a destra
            robot.right()
        else:
            print("neutro")
            robot.stop()  # Se il messaggio non è riconosciuto, il robot si ferma

if __name__ == "__main__":  # Controlla se lo script è eseguito direttamente
    main()  # Esegue la funzione principale