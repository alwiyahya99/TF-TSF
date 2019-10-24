import cv2
import numpy as np

image = cv2.imread("PlatNomor.jpg")
cv2.imshow("imageOri", image)
cv2.waitKey(0)

gray = cv2.ovtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
print(gray)
cv2.waitKey(0)

