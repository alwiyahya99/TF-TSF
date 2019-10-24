import cv2
import numpy as np

# Read image.
img = cv2.imread("example.jpg")
cv2.imshow("imageOri", img)
cv2.waitKey(0)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))

#Thresholding
ret,theshold = cv2.threshold(gray_blurred,70,255,cv2.THRESH_BINARY)
cv2.imshow("Theshold", theshold)
cv2.waitKey(0)

# Apply Hough transform on the blurred image.
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1.2, 100)

# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(gray_blurred, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(gray_blurred, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # show the output image
    cv2.imshow("output", np.hstack([img, theshold]))
    cv2.waitKey(0)
