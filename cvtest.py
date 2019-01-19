import numpy as np
import cv2

face_cascade_path = '/usr/local/opt/opencv/share/opencv4/haarcascades/haarcascade_frontlface_default.xml'
img_path = ''
face_cascade = cv2.CascadeClassifire('haarcascade_frontlface_default.xml')
img = cv2.imread('test.jpg')