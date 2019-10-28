# import numpy as np
# import cv2
#
# from utils
#
# cap = cv2.VideoCapture(0)
#
# face_cascade = cv2.CascadeClassifier('OpenCV-Python-Series-master\OpenCV-Python-Series-master\src\cascades\data\haarcascade_frontalface_alt2.xml')
# eye_cascade = cv2.CascadeClassifier('OpenCV-Python-Series-master\OpenCV-Python-Series-master\src\cascades\dthird-party\hfrontalEyes35x16.xml')
# smile_cascade = cv2.CascadeClassifier('OpenCV-Python-Series-master\OpenCV-Python-Series-master\src\cascades\dthird-party\hNose18x15.xml')
# glasses = cv2.imread('OpenCV-Python-Series-master\OpenCV-Python-Series-master\src\images\fun\glasses.png')
# glasses = cv2.imread('OpenCV-Python-Series-master\OpenCV-Python-Series-master\src\images\fun\gmustache.png')
#
#
# while True:
#     # mendeteksi frame-by-frame
#     ret, frame = cap.read()
#
#     #display the resulting frame
#     out.write(frame)
#