from flask import Flask, Response

from camera import webcam_face_detect
import flask_cors
import sys
import logging

cors = flask_cors.CORS()
app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
cors.init_app(app, resources={r"/*": {"origins": "*"}})


@app.route("/viewer")
def prediction_controller():
    if len(sys.argv) >= 2:
        video_mode = sys.argv[1]
    else:
        video_mode = 0
    return Response(webcam_face_detect(video_mode), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
