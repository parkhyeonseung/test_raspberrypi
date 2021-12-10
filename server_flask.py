from flask import Flask
from flask import request
from flask import Response
from flask import render_template
import cv2

app = Flask(__name__)
# cap = cv2.VideoCapture(gstreamer_pipeline(),cv2.CAP_GSTREAMER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/video_feed")
def video_feed():
    return Response(stream_gen(cv2.VideoCapture(0)), mimetype='multipart/x-mixed-replace; boundary=frame')

def stream_gen(cap):
    while True:
        try:
            success, frame = cap.read()  # read the camera frame
            frame = cv2.resize(frame,(600,600))
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpeg', frame)
                # frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + bytearray(buffer) + b'\r\n') 
        except KeyboardInterrupt:
            cap.realease()
            break
        except :
            pass

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8000)