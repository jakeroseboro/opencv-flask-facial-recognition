import cv2


def webcam_face_detect(video_mode, nogui=False, cascasdepath="haarcascade_frontal_face_default.xml"):
    face_cascade = cv2.CascadeClassifier(cascasdepath)

    video_capture = cv2.VideoCapture(video_mode)
    num_faces = 0

    while True:
        ret, image = video_capture.read()

        if not ret:
            break

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)

        )
        num_faces = len(faces)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + h, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (x, y)
            fontScale = 1  # (try differnt values)
            color = (0, 255, 0)
            thickness = 2  # (try differnt values)
            cv2.putText(image, "faces found: " + str(num_faces), org, font,
                                fontScale, color, thickness, cv2.LINE_AA)

            #cv2.imshow("Faces found", image)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                #break

        ret, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    #video_capture.release()
    #cv2.destroyAllWindows()
    #return num_faces
