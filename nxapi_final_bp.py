import requests
import nxapilib

hostname = '192.168.47.102'
username = 'admin'
password = 'admin'

source_vlan = '500'
target_vlan = '800'
desc = 'FOO'
desired_interfaces = []

# Step 1: List all desired_interfaces
response = nxapilib.nxapi_request(hostname, username, password, ['show int status'])

for interface in response.json()['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']:
    if interface['vlan'] == source_vlan and interface.get('name') == desc:
        desired_interfaces.append(interface['interface'])

# Step 2: Creating target_vlan and adding desired_interfaces to target_vlan
commands = [f'vlan {target_vlan}']
for interface in desired_interfaces:
    commands.append(f'int {interface}')
    commands.append(f'switchport access vlan {target_vlan}')

response = nxapilib.nxapi_request(hostname, username, password, commands, command_type='cli_conf')
if nxapilib.nxapi_verify_response(response):
    print('TASK DONE!')
