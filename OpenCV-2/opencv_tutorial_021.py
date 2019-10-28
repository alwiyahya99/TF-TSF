import argparse
import imutils
import cv2

# construct the argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
Blur = cv2.GaussianBlur(gray, (3, 3), 0)
cany = cv2.Canny(Blur, 20, 100)
cv2.imshow("Cany", cany)
cv2.waitKey(0)

# mencari kontur dari gambar yang telah di threshold
# cnts = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts, hierarchy = cv2.findContours(cany.copy(),cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts:
    # menggambar kontur setiap object dengan ketebalan garis 3px
    cv2.drawContours(output, [c], -1, (0, 255, 250), 3)
    cv2.imshow("Contours", output)

cv2.waitKey(0)