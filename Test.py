import RPi.GPIO as GPIO
import keyboard  # Libreria per leggere input da tastiera
import time

class AlphaBot(object):
    def __init__(self, in1=12, in2=13, ena=6, in3=20, in4=21, enb=26):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENA = ena
        self.ENB = enb

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        self.PWMA = GPIO.PWM(self.ENA, 500)
        self.PWMB = GPIO.PWM(self.ENB, 500)
        self.PWMA.start(50)
        self.PWMB.start(50)

    def forward(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def backward(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

    def left(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

    def right(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

def main():
    robot = AlphaBot()
    print("Usa le frecce direzionali o i tasti WASD per muovere l'AlphaBot. Premi 'Q' per uscire.")

    try:
        while True:
            if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
                robot.forward()
            elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
                robot.backward()
            elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):
                robot.left()
            elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):
                robot.right()
            else:
                robot.stop()
            
            if keyboard.is_pressed('q'):  # Esci premendo 'Q'
                print("Chiusura...")
                break
            
            time.sleep(1)  # Piccola pausa per evitare input troppo rapidi

    except KeyboardInterrupt:
        print("Interrotto dall'utente")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
