from nxapilib import *

with open('hosts.txt') as f:
    hosts = f.read().split()

for host in hosts:

    username = 'admin'
    password = 'admin'

    commands = [
    'hostname SW1',
    ]

    response = nxapi_request(host, username, password, commands, command_type='cli_conf')
    print(response.text)
