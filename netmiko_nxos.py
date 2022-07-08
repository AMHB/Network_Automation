from netmiko import ConnectHandler

nxos = {'device_type': 'cisco_nxos',
        'host':   '192.168.47.102',
        'username': 'admin',
        'password': 'admin',
        'port' : 22}

conn = ConnectHandler(**nxos)

output = conn.send_command('show int status', use_textfsm=True)
output = conn.send_command('show int status | json-pretty')
for interface in output:
    print(interface['port'])

conn.disconnect()
