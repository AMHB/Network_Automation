from nxapilib import *

host = '192.168.47.102'
username = 'admin'
password = 'admin'


response = nxapi_request(host, username, password, ['show int desc'], command_type='cli_show')
for interface in response.json()['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']:
    print(interface['interface'])
