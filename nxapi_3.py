from nxapilib import *

host = '192.168.47.102'
username = 'admin'
password = 'admin'

commands = [
'hostname FOOSW',
'hostname FOOSW1',
]

response = nxapi_request(host, username, password, commands,
                        command_type='cli_conf', rollback='stop-on-error')
if nxapi_verify_response(response):
    print('ALL OK!')
