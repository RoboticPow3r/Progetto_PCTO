import cv2
from flask import Flask, Response

# Inizializza l'app Flask
app = Flask(__name__)

# Cattura il video dalla videocamera (ad esempio la videocamera USB)
cap1 = cv2.VideoCapture(1)  # Telecamera 1 (modifica se necessario)

# Funzione per generare il flusso video dalla prima videocamera
def generate_frames1():
    while True:
        success, frame = cap1.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()  # Converte l'immagine in un byte array
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Route per il flusso video
@app.route('/video')
def video_feed1():
    return Response(generate_frames1(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Avvia il server Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


