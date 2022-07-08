import socket
import gzip
import re
import sys

url = sys.argv[1]

m = re.search(r'http://(.+?)(/.+)', url)
host = m.groups()[0]
path = m.groups()[1]
filename = path.split('/')[-1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 80))

http_request_lines = [
f'GET {path} HTTP/1.1',
f'Host: {host}',
'Connection: close',
'Accept-Encoding: gzip',
]

http_request = '\r\n'.join(http_request_lines) + '\r\n\r\n'

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

with open(filename, 'wb') as f:
    f.write(content_decompressed)

s.close()
