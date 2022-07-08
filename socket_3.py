import socket
import gzip

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('95.216.206.241', 80))

http_request_lines = [
'GET /foobar1.html HTTP/1.1',
'Host: 95.216.206.241',
'Connection: close',
'Accept-Encoding: gzip',
]

http_request = '\r\n'.join(http_request_lines) + '\r\n\r\n'
print(http_request)

s.send(http_request.encode())
response = s.recv(1024)

newline_index = response.index(b'\r\n\r\n')
header = response[0:newline_index]
content = response[newline_index + 4:]
content_decompressed = gzip.decompress(content)

print(header.decode())
print()
print(content_decompressed.decode())
s.close()
