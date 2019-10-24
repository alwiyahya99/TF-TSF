# import socket
#
# # CREATE TCP/IP socket
# stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# host = '192.168.43.38'
# port = 8080
# server_adress = ((host,port))
# print("connecting")
# stream_socket.connect(server_adress)
#
# #Mengirim data
# pesan = 'message'
# stream_socket.sendall(pesan)
#
# #Response
# data = stream_socket.recv(10)
# print(data)
#
# print('socket ditutup')
# stream_socket.close()

import socket
import sys

# Create a TCP/IP socket
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host
ip = socket.gethostbyname("www.google.com")
print(ip)
host = '192.168.43.38'

# define the communication port
port = 8080
try:
        # Connect the socket to the port where the server is listening
        server_address = ((host, port))

        print("connecting")

        stream_socket.connect(server_address)
        while True:
            # Send data
            message = 'message'
            stream_socket.sendall(message)

            # response
            data = stream_socket.recv(10)
            print(data)
except:
        print('mencari koneksi')
print('socket closed')
stream_socket.close()