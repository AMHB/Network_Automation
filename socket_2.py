import socket

# http://payment.uast.ac.ir/login.php

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('payment.uast.ac.ir', 80))

http_request_lines = [
'GET /login.php HTTP/1.1',
'Host: payment.uast.ac.ir',
'Connection: close',
]

http_request = '\r\n'.join(http_request_lines) + '\r\n\r\n'
print(http_request)

s.send(http_request.encode())

response = b''
while True:
    chunk = s.recv(1024)
    if not chunk:
        break
    response += chunk

print(http_request)



newline_index = response.index(b'\r\n\r\n')
header = response[0:newline_index]
content = response[newline_index + 4:]

print(header.decode())
print(len(content))


s.close()
