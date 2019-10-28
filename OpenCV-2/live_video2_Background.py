import cv2

videoCamp = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('OpenCV-Python-Series-master\OpenCV-Python-Series-master\src\cascades\data\haarcascade_frontalface_default.xml')

# menghilangkan background jadi hitam
bg = cv2.createBackgroundSubtractorMOG2()
while True:
    cond, frame = videoCamp.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    ret, theshold = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)
    edged = cv2.Canny(theshold, 70, 250)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    fgb = bg.apply(closed)

    cnts, hierarchy = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    output = frame.copy()

    # menggambar contour
    for c in cnts:
        # menggambar kontur setiap object dengan ketebalan garis 3px
        cv2.drawContours(output, [c], -1, (0, 255, 250), 3)
        cv2.imshow("Contours", output)

    cv2.imshow('Background', fgb)
    # cv2.imshow('Blur', blur)
    # cv2.imshow('Face Detect', frame)

    exit = cv2.waitKey(1) & 0xff
    if exit == ord('1'):
        break

videoCamp.release()
cv2.destroyAllWindows()