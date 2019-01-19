import cv2
import cvconfig

face_cascade = cv2.CascadeClassifier(cvconfig.FACE_CASCADE_PATH)
img = cv2.imread(cvconfig.IMG_PATH)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray , 1.1, 30)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    face = img[y: y + h, x: x + w]
    face_gray = img_gray[y: y + h, x: x + w]
    
cv2.imwrite(cvconfig.RESULT_PATH, img)

