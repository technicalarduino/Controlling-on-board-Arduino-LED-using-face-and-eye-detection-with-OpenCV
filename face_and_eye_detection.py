import cv2
import numpy as np
import serial
import time

Myserial = serial.Serial('COM4', 9600)
time.sleep(2) # waiting the initialization...
print("initialised")

# loading in the cascades.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Using the device's default camera for video capture.
cap = cv2.VideoCapture(0)

# detection and drawing rectangles
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    # Press 'ESC' to release the camera.
    cv2.imshow('img', img)
    if (len(faces)) == 0:
      Myserial.write(str.encode('0'))
      print("No face is detected")
    elif (len(faces)) == 1:
      Myserial.write(str.encode('Yes'))
      print("Face is detected")

    k = cv2.waitKey(30)&0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()