import cv2

face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
cam = cv2.VideoCapture(0)
jumlah = 0
id = input("Masukan ID : ")

while True:
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    muka = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for(x, y, w, h) in muka:
        if cv2.waitKey(1) & 0xff == ord('c'):
            #User. + id. + serial (jumlah)
            cv2.imwrite('data-wajah/User.'+ id + '.' + str(jumlah) + ".jpg", gray[y:y+h, x:x+w])
            jumlah += 1

    cv2.imshow('Capturing', frame)

    if jumlah > 20:
        break

cam.release()
cv2.destroyAllWindows()