import cv2
import pickle
import numpy as np
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Initialize camera
video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Load face detection model
face_cascade_path = 'data/haarcascade_frontalface_default.xml'
facedetect = cv2.CascadeClassifier(face_cascade_path)
if facedetect.empty():
    print(f"Error: Could not load cascade classifier from {face_cascade_path}.")
    exit()

faces_data = []
i = 0

name = input("Enter Your Name: ")
print("Capturing face data. Please stay in front of the camera...")

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten()
        
        if len(faces_data) < 100 and i % 10 == 0:
            faces_data.append(resized_img)
        i += 1
        
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
    
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) == 100:
        break

print("Face data collection complete.")
video.release()
cv2.destroyAllWindows()

faces_data = np.asarray(faces_data).reshape(len(faces_data), -1)

# Handle names.pkl
names_file = 'data/names.pkl'
if os.path.exists(names_file):
    with open(names_file, 'rb') as f:
        names = pickle.load(f)
else:
    names = []

names += [name] * len(faces_data)
with open(names_file, 'wb') as f:
    pickle.dump(names, f)

# Handle faces.pkl
faces_file = 'data/faces.pkl'
if os.path.exists(faces_file):
    with open(faces_file, 'rb') as f:
        faces = pickle.load(f)
    faces = np.vstack((faces, faces_data))
else:
    faces = faces_data

with open(faces_file, 'wb') as f:
    pickle.dump(faces, f)

print("Face data saved successfully.")
