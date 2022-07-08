import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000))

#data = s.recv(1024)
# print(data.decode())
s.send('hello from tcp client\n'.encode())



s.close()
