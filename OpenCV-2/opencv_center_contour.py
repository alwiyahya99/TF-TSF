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
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)# mengubah gambar menjadi warna abu-abu
Blur = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(Blur, 70, 255, cv2.THRESH_BINARY_INV)[1]# threshold atau merubah gambar yang di dalam garis tepian menjadi warna putih

mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
cv2.waitKey(0)

# mencari kontur dari gambar yang telah di threshold
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts:
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
    cv2.circle(output, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(output, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # menampilkan hasil proses
    cv2.imshow("Contours", output)
    cv2.waitKey(0)