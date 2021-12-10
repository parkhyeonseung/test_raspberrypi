from flask import Flask
import cv2
import threading
from flask import Response

app = Flask(__name__)
frame = ''
@app.route('/')
def index():
    str = 'hello'
    return str


@app.route('/streaming')
def streamframe():
    return Response(stream(cv2.VideoCapture(0)), mimetype='multipart/x-mixed-replace; boundary=frame')

def stream(cap):
    global frame
    while True:
        try:
            ret,frame = cap.read()
            frame = cv2.resize(frame,(960,800))
            if not ret:break
            # cv2.imshow('a',frame)
            else:
                ret,encoded_image = cv2.imencode('.jpeg',frame)
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')
        except KeyboardInterrupt:
            cap.release()
            break
        except :
            pass


if __name__ == '__main__':
    cam = threading.Thread(target = stream,args=(cv2.VideoCapture(0),))
    cam.daemon = True
    cam.start()
    app.run(host = '0.0.0.0',port = 8000)
    
    pass