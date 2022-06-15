from flask import Flask, Response, render_template

from camera import webcam_face_detect
import flask_cors
import sys
import logging

cors = flask_cors.CORS()
app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
cors.init_app(app, resources={r"/*": {"origins": "*"}})


@app.route("/facial_recognition")
def facial_recognition():
    if len(sys.argv) >= 2:
        video_mode = sys.argv[1]
    else:
        video_mode = 0
    return Response(webcam_face_detect(video_mode), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/facial_recognition_demo")
def facial_recognition_demo():
    return render_template('facial_recognition.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
