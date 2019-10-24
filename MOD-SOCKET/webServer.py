import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"anda terhubung dengan alamat {address}")
    masukan = input("Tuliskan Pesan : ")
    clientsocket.send(bytes(masukan,"utf-8"))
    clientsocket.close()

    sw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sw.connect((socket.gethostname(), 12345))
    msg = sw.recv(1024)
    print("Pesan Masuk : ", msg.decode("utf-8"))