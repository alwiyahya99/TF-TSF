import socket

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    msg = s.recv(1024)
    print("Pesan Masuk : ",msg.decode("utf-8"))

    sw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sw.bind((socket.gethostname(), 12345))
    sw.listen(5)
    clientsocket, address = sw.accept()

    print(f"anda terhubung dengan alamat {address}")
    masukan = input("Tuliskan Pesan : ")
    clientsocket.send(bytes(masukan, "utf-8"))
    clientsocket.close()