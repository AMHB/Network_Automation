from netmiko import ConnectHandler

# conn = ConnectHandler(device_type='cisco_ios',
#                       host='192.168.47.101',
#                       username='cisco',
#                       password='cisco',
#                       secret='cisco',
#                       port=22)

ios = {'device_type': 'cisco_ios',
       'host':   '192.168.47.101',
       'username': 'cisco',
       'password': 'cisco',
       'secret': 'cisco',
       'port' : 22}

conn = ConnectHandler(**ios)

conn.enable()
# output = conn.send_command('show int f0/0')
# print(output)

# commands = ['int lo4', 'desc LO FOUR', 'ip address 4.4.4.4 255.255.255.0']
# conn.send_config_set(commands)
# conn.send_config_from_file('commands.txt')

print(conn.find_prompt())
conn.disconnect()
