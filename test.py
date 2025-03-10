import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch
from sklearn.neighbors import KNeighborsClassifier


def speak(text):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

# Initialize camera and face detector
video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Error: Could not open webcam.")
    exit()

facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
if facedetect.empty():
    print("Error: Could not load face detection model.")
    exit()

# Load trained face data
try:
    with open('data/names.pkl', 'rb') as w:
        LABELS = pickle.load(w)
    with open('data/faces.pkl', 'rb') as f:
        FACES = pickle.load(f)
    print('Shape of Faces matrix -->', FACES.shape)
except FileNotFoundError:
    print("Error: Face data files not found. Run add_faces.py first.")
    exit()

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

imgBackground = cv2.imread("background.png")
COL_NAMES = ['NAME', 'TIME']

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
file_path = f"Attendance/Attendance_{date}.csv"
os.makedirs("Attendance", exist_ok=True)

attendance = None  # Ensure attendance is always defined

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        
        timestamp = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
        attendance = [str(output[0]), str(timestamp)]
        
        # Draw on frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
    
    imgBackground[162:642, 55:695] = frame
    cv2.imshow("Frame", imgBackground)
    k = cv2.waitKey(1)
    
    if k == ord('o') and attendance:
        speak("Attendance Taken..")
        time.sleep(5)
        
        file_exists = os.path.isfile(file_path)
        
        with open(file_path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists or os.stat(file_path).st_size == 0:
                writer.writerow(COL_NAMES)
            writer.writerow(attendance)
    
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
