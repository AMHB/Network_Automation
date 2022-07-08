import cisco_ssh
import re

host = '192.168.47.101'
username = 'cisco'
password = 'cisco'
secret = 'cisco'

shell = cisco_ssh.ssh_connect(host, username, password)
cisco_ssh.send(shell, 'terminal length 0')
cisco_ssh.send(shell, 'enable')
cisco_ssh.send(shell, secret)

loopbacks = [
    {'n':'1', 'ipaddr': '1.1.1.1', 'mask': '255.255.255.0', 'desc':'LO ONE'},
    {'n':'2', 'ipaddr': '2.2.2.2', 'mask': '255.255.255.0', 'desc':'LO TWO'},
    {'n':'3', 'ipaddr': '3.3.3.3', 'mask': '255.255.255.0', 'desc':'LO THREE'},
]

commands = ['conf t']
for lo in loopbacks:
    commands.append(f'int Lo{lo["n"]}')
    commands.append(f'desc {lo["desc"]}')
    commands.append(f'ip address {lo["ipaddr"]} {lo["mask"]}')
    commands.append('exit')

for command in commands:
    cisco_ssh.send(shell, command)
