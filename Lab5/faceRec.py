# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html

import cv2
import numpy as np

training = []
testing = []

path = '/home/echeng/Documents/COEN166/Lab5/att_faces_10/att_faces_10/s1/1.pgm'
img = cv2.imread(path)

cv2.imshow('image', img)
cv2.waitKey(0)
