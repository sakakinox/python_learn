import numpy as np
import cv2

face_cascade_path = '/usr/local/opt/opencv/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
img_path = 'test.jpg'
result_path ='result.jpg'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray , 1.1, 30)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    face = img[y: y + h, x: x + w]
    face_gray = img_gray[y: y + h, x: x + w]
    
cv2.imwrite(result_path, img)

