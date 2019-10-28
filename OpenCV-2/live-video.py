import cv2

videoCamp = cv2.VideoCapture(0)
herp = cv2.imread('herp.png', -1)

face_cascade = cv2.CascadeClassifier('OpenCV-Python-Series-master\OpenCV-Python-Series-master\src\cascades\data\haarcascade_frontalface_default.xml')

# menghilangkan background jadi hitam
# bg = cv2.createBackgroundSubtractorMOG2()
while True:
    cond, frame = videoCamp.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 5)
    cany = cv2.Canny(blur, 60, 90)
    # fgb = bg.apply(gray)
    face = face_cascade.detectMultiScale(blur, 1.3, 5)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # blur = cv2.GaussianBlur(frame, (3, 3), 0)
    # edge = cv2.Canny(blur, 70, 70)
    # cv2.imshow('Background', fgb)
    cv2.imshow('Blur', blur)
    cv2.imshow('Face Detect', frame)

    exit = cv2.waitKey(1) & 0xff
    if exit == ord('1'):
        break

videoCamp.release()
cv2.destroyAllWindows()