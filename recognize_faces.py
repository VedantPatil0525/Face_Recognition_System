import cv2
import pickle
import face_recognition
import numpy as np
import time
import csv
from datetime import datetime
import os

SCREENSHOT_DIR = "Screenshots"

if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

# Load encodings
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

markes_names = set()

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video.isOpened():
    print("❌ Webcam not accessible")
    exit()

face_detected = False
detection_time = None
screenshot_taken = False

SCANNED_FACES = "scanned.csv"

def scan_face(name):
    now = datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    # If file does not exist, create it and add header
    if not os.path.exists(SCANNED_FACES):
        with open(SCANNED_FACES, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['Name','Date','Time'])

    # Read existing faces
    with open(SCANNED_FACES, 'r') as f:
        reader = csv.reader(f)
        records = list(reader)

    # Check for duplicate entry (same name & same date)
    for row in records[1:]:
        if row[0] == name and row[1] == today_date:
            print(f"Face already scanned for {name} today.")
            return
        
    # Append new face entry
    with open(SCANNED_FACES, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, today_date, current_time])

    print(f"Face scanned for {name} at {current_time}!!")

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

            # Scan face and add in csv file
            if name not in markes_names:
                markes_names.add(name)
                scan_face(name)

            # 🔑 START TIMER WHEN FACE IS DETECTED
            if not face_detected:
                face_detected = True
                detection_time = time.time()

            # Take Screenshot
            if not screenshot_taken:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{name}_{timestamp}.png"
                filepath = os.path.join(SCREENSHOT_DIR, filename)

                cv2.imwrite(filepath, frame)
                screenshot_taken = True

                print(f"Screenshot saved: {filepath}")

        top, right, bottom, left = box
        top *= 2; right *= 2; bottom *= 2; left *= 2

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Face Recognition System", frame)

    # 🔒 CLOSE WINDOW AFTER 5 SECONDS OF DETECTION
    if face_detected and (time.time() - detection_time >= 5):
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
