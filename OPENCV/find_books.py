# import the necessary packages
import numpy as np
import cv2

# load the image
image = cv2.imread("example.jpg")
cv2.imshow("imageOri", image)
cv2.waitKey(0)

# convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

#Bluring image
Blur = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imshow("Blur", Blur)
cv2.waitKey(0)

#Thresholding
ret,theshold = cv2.threshold(Blur,70,255,cv2.THRESH_BINARY)
cv2.imshow("Theshold", theshold)
cv2.waitKey(0)

img=0

# detect edges in the image
edged = cv2.Canny(theshold, 10, 250)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

# construct and apply a closing kernel to 'close' gaps between 'white'
# pixels
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
cv2.waitKey(0)

# find contours (i.e. the 'outlines') in the image and initialize the
# total number of books found
#EDIT==>(cnts, _,) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts, hierarchy = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
total = 0

# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# if the approximated contour has four points, then assume that the
	# contour is a book -- a book is a rectangle and thus has four vertices
	if len(approx) == 4:
		if cv2.contourArea(c) > 100:
			total += 1
			cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)


# display the output
print ("I found {0} books in that image".format(total))
cv2.imshow("Output", image)
cv2.waitKey(0)