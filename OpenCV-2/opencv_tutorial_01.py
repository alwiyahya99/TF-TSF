import imutils
import cv2

image = cv2.imread("jp.png") # load the input image and show its dimensions, keeping in mind that
(h,w,d) = image.shape
print("height = {}, width = {}, depth = {}".format(h,w,d))# menampilkan (h = height'baris', w = width'kolom', d = depth)
# cv2.imshow("Image", image) #menampilkan gambar jp.png
# cv2.waitKey(0)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R = {}, G = {}, B = {}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[60:160, 320:420]
# cv2.imshow("ROI", roi)
# cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0/ w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
# cv2.imshow("Fixing Resizing", resized)
# cv2.waitKey(0)

# fix mengubah ukuran menggunakan library imutils
resized = imutils.resize(image, width = 300)
# cv2.imshow("Fixing Resizing Imutils Library", resized)
# cv2.waitKey(0)

#menghaluskan gambar atau menjadikan gambar nampak blur
# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11,11),0)
# cv2.imshow("Burred", blurred)
# cv2.waitKey(0)

#menggambar persegi panjang merah tebal 2px yang melengkapi wajah
output = image.copy()
cv2.rectangle(output, (550, 90), (490, 170), (0,0,255), 2)#kotak yang laki kanan
cv2.rectangle(output, (320, 60), (420, 160), (0,0,255), 2)#kotak yang laki tengah
cv2.rectangle(output, (120, 220), (280, 60), (0,0,255), 2) #kotak yang cewe
cv2.imshow("kotak", output)
cv2.waitKey(0)

ou = image.copy()
GR = cv2.cvtColor(ou, cv2.COLOR_BGR2GRAY)
cv2.imshow("grey", GR)

blurred = cv2.GaussianBlur(GR, (11,11),0)
cv2.imshow("blur", blurred)

thres = cv2.threshold(blurred, 75, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("threshold", thres)
cv2.waitKey(0)

#menggambar text pada gambar dengan warna hijau
output = image.copy()
cv2.putText(output, "OpenCV + Jurasik Park!!", (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
# cv2.imshow("memberi text pada gambar", output)
# cv2.waitKey(0)