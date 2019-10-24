import argparse
import imutils
import cv2

# construct the argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

# menampilkan gambar
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# mengubah gambar menjadi warna abu-abu
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gambar abu-abu", gray)
cv2.waitKey(0)

Blur = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Blur", Blur)
cv2.waitKey(0)

# threshold atau merubah gambar yang di dalam garis tepian menjadi warna putih
thresh = cv2.threshold(Blur, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)

# # mendeteksi tepian dari objeck yang digambar
# edge = cv2.Canny(thresh, 10, 150)
# cv2.imshow("Deteksi Tepian(Edge)", edge)
# cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
cv2.waitKey(0)

# mencari kontur dari gambar yang telah di threshold
# cnts = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts, hierarchy = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts:
    # menggambar kontur setiap object dengan ketebalan garis 3px
    cv2.drawContours(output, [c], -1, (0, 255, 250), 3)
    cv2.imshow("Contours", output)

cv2.waitKey(0)