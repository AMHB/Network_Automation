import socket
import gzip
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('95.216.206.241', 80))

http_request_lines = [
'GET /kitcat.png HTTP/1.1',
'Host: 95.216.206.241',
'Connection: close',
'Accept-Encoding: gzip',
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

newline_index = response.index(b'\r\n\r\n')
header = response[0:newline_index]
content = response[newline_index + 4:]

if re.search(r'content-encoding: gzip', header.decode(), re.I):
    content_decompressed = gzip.decompress(content)
else:
    content_decompressed = content

print(header.decode())
print()
print(len(content))

with open('kitcat.png', 'wb') as f:
    f.write(content_decompressed)

s.close()
