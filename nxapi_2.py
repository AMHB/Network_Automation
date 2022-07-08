from nxapilib import *

host = '192.168.47.102'
username = 'admin'
password = 'admin'


response = nxapi_request(host, username, password, ['show int mgmt0'], command_type='cli_show')
print(response.text)
