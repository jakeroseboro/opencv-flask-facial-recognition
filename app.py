from flask import Flask, Response, render_template
from flask_bootstrap import Bootstrap
from camera import webcam_face_detect
from witch_filter import witch_filter
import flask_cors
import sys
import logging

app = Flask(__name__)
cors = flask_cors.CORS()
Bootstrap(app)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
cors.init_app(app, resources={r"/*": {"origins": "*"}})


@app.route("/facial_recognition")
def facial_recognition():
    if len(sys.argv) >= 2:
        video_mode = sys.argv[1]
    else:
        video_mode = 0
    return Response(webcam_face_detect(video_mode), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/witch_demo")
def witch_filter_demo():
    if len(sys.argv) >= 2:
        video_mode = sys.argv[1]
    else:
        video_mode = 0
    return Response(witch_filter(video_mode), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/witch_filter_demo")
def witch_filter_template():
    return render_template('witch_demo.html')


@app.route('/')
def index():
    return render_template('facial_recognition.html')


if __name__ == '__main__':
    app.run()
