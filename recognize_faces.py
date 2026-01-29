import cv2
import pickle
import face_recognition
import numpy as np
import time
# from PIL import Image

# Load encodings
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video.isOpened():
    print("❌ Webcam not accessible")
    exit()

face_detected = False
detection_time = None

while True:
    ret, frame = video.read()
    if not ret:
        continue

    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding, box in zip(encodings, boxes):
        matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.5)
        name = "Unknown"

        if True in matches:
            name = data["names"][matches.index(True)]

            # 🔑 START TIMER WHEN FACE IS DETECTED
            if not face_detected:
                face_detected = True
                detection_time = time.time()

        top, right, bottom, left = box
        top *= 2; right *= 2; bottom *= 2; left *= 2

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Face Recognition System", frame)

    # 🔒 CLOSE WINDOW AFTER 5 SECONDS OF DETECTION
    if face_detected and (time.time() - detection_time >= 10):
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
