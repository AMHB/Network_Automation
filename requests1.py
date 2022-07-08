import requests
import gzip

response = requests.get('https://arjang.ac.ir/')
print(response.status_code)
for k, v in response.headers.items():
    print(f'{k}: {v}')

c = response.content
c = response.text

print(c)
