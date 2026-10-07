# My-first-repository
Just to know how things work
AI Crowd Monitoring System

Author: Ayush Kushwaha (Sample Project)

Description: A basic crowd monitoring system using OpenCV and Python.

> **Project status:** Educational prototype for learning computer-vision based crowd detection.

Features:

- Detect people in video using HOG + SVM
- Count people in each frame
- Raise alert if crowd exceeds a threshold

import cv2 import imutils from datetime import datetime

------------------ Configuration ------------------

VIDEO_SOURCE = 0  # 0 for webcam, or path to video file CROWD_LIMIT = 10  # Threshold for crowd alert

------------------ Initialize HOG Person Detector ------------------

hog = cv2.HOGDescriptor() hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

------------------ Video Capture ------------------

cap = cv2.VideoCapture(VIDEO_SOURCE)

if not cap.isOpened(): print("Error: Video source not accessible") exit()

print("Crowd Monitoring Started...")

------------------ Main Loop ------------------

while True: ret, frame = cap.read() if not ret: break

frame = imutils.resize(frame, width=800)

# Detect people
(regions, _) = hog.detectMultiScale(frame,
                                     winStride=(4, 4),
                                     padding=(8, 8),
                                     scale=1.05)

people_count = len(regions)

# Draw bounding boxes
for (x, y, w, h) in regions:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display crowd count
cv2.putText(frame, f"People Count: {people_count}",
            (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 0, 0), 2)

# Alert if crowd limit exceeded
if people_count > CROWD_LIMIT:
    cv2.putText(frame, "ALERT: CROWD LIMIT EXCEEDED!",
                (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (0, 0, 255), 3)
    print(f"[{datetime.now()}] ALERT: Crowd limit exceeded")

cv2.imshow("AI Crowd Monitoring", frame)

# Press 'q' to quit
if cv2.waitKey(1) & 0xFF == ord('q'):
    break

------------------ Cleanup ------------------

cap.release() cv2.destroyAllWindows() print("Crowd Monitoring Stopped")

------------------ Requirements ------------------

pip install opencv-python imutils
